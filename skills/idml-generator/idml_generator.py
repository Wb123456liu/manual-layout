#!/usr/bin/env python3
"""
IDML Generator - 将 HTML/CSS 转换为 Adobe InDesign IDML 格式
"""

import zipfile
import os
import uuid
from datetime import datetime
from pathlib import Path


class IDMLGenerator:
    """IDML 文档生成器"""
    
    def __init__(self, document_name="Document", page_size="A4", language="zh-CN"):
        self.document_name = document_name
        self.page_size = page_size
        self.language = language
        self.styles = {}
        self.pages = []
        self.stories = []
        self.spreads = []
        
        # 页面尺寸 (points)
        self.page_sizes = {
            "A4": (595.28, 841.89),
            "A3": (841.89, 1190.55),
            "Letter": (612, 792)
        }
        
        # 默认边距 (points)
        self.margins = {
            "top": 56.69,    # 20mm
            "bottom": 42.52, # 15mm
            "left": 28.35,   # 10mm
            "right": 28.35   # 10mm
        }
        
        # 样式计数器
        self._style_counter = 0
        self._story_counter = 0
        self._spread_counter = 0
    
    def add_paragraph_style(self, name, properties):
        """添加段落样式"""
        self.styles[name] = {
            "type": "paragraph",
            "properties": properties
        }
    
    def add_character_style(self, name, properties):
        """添加字符样式"""
        self.styles[name] = {
            "type": "character",
            "properties": properties
        }
    
    def add_page(self, content):
        """添加页面内容"""
        self.pages.append(content)
    
    def _generate_id(self, prefix="u"):
        """生成唯一 ID"""
        self._style_counter += 1
        return f"{prefix}{self._style_counter:x}"
    
    def _generate_mimetype(self):
        """生成 mimetype 文件"""
        return "application/vnd.adobe.indesign-idml"
    
    def _generate_container_xml(self):
        """生成 META-INF/container.xml"""
        return '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="designmap.xml" media-type="text/xml"/>
    </rootfiles>
</container>
'''
    
    def _generate_designmap_xml(self):
        """生成 designmap.xml - 文档主文件"""
        width, height = self.page_sizes.get(self.page_size, self.page_sizes["A4"])
        
        return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<?aid style="50" type="document" readerVersion="6.0" featureSet="257" product="20.4(52)" ?>
<Document xmlns:idPkg="http://ns.adobe.com/AdobeInDesign/idml/1.0/packaging" 
          DOMVersion="20.4" 
          Self="d" 
          Name="{self.document_name}.indd" 
          ZeroPoint="0 0"
          CMYKProfile="Japan Color 2001 Coated"
          RGBProfile="sRGB IEC61966-2.1">
    <Properties>
        <Label>
            <KeyValuePair Key="kAdobeDPS_Version" Value="2" />
        </Label>
    </Properties>
    <idPkg:Styles src="Resources/Styles.xml" />
    <idPkg:Fonts src="Resources/Fonts.xml" />
    <idPkg:Preferences src="Resources/Preferences.xml" />
</Document>
'''
    
    def _generate_styles_xml(self):
        """生成 Resources/Styles.xml"""
        styles_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<idPkg:Styles xmlns:idPkg="http://ns.adobe.com/AdobeInDesign/idml/1.0/packaging" DOMVersion="20.4">
    <RootCharacterStyleGroup Self="u7e">
        <CharacterStyle Self="CharacterStyle/$ID/[No character style]" 
                       Name="$ID/[No character style]" 
                       Imported="false" 
                       SplitDocument="false" 
                       EmitCss="true" />
'''
        
        # 添加自定义字符样式
        for name, style in self.styles.items():
            if style["type"] == "character":
                props = style["properties"]
                font = props.get("font", "Arial")
                size = props.get("size", 10)
                
                styles_xml += f'''
        <CharacterStyle Self="CharacterStyle/{name}" 
                       Name="{name}" 
                       FontStyle="Regular" 
                       PointSize="{size}">
            <Properties>
                <BasedOn type="string">$ID/[No character style]</BasedOn>
                <AppliedFont type="string">{font}</AppliedFont>
            </Properties>
        </CharacterStyle>
'''
        
        styles_xml += '''
    </RootCharacterStyleGroup>
    <RootParagraphStyleGroup Self="u7d">
        <ParagraphStyle Self="ParagraphStyle/$ID/[No paragraph style]" 
                       Name="$ID/[No paragraph style]" />
'''
        
        # 添加自定义段落样式
        for name, style in self.styles.items():
            if style["type"] == "paragraph":
                props = style["properties"]
                font = props.get("font", "Arial")
                size = props.get("size", 10)
                leading = props.get("leading", size * 1.2)
                space_after = props.get("space_after", 0)
                
                styles_xml += f'''
        <ParagraphStyle Self="ParagraphStyle/{name}" 
                       Name="{name}" 
                       FontStyle="Regular" 
                       PointSize="{size}"
                       SpaceAfter="{space_after}">
            <Properties>
                <BasedOn type="string">$ID/[No paragraph style]</BasedOn>
                <Leading type="unit">{leading}</Leading>
                <AppliedFont type="string">{font}</AppliedFont>
            </Properties>
        </ParagraphStyle>
'''
        
        styles_xml += '''
    </RootParagraphStyleGroup>
</idPkg:Styles>
'''
        return styles_xml
    
    def _generate_fonts_xml(self):
        """生成 Resources/Fonts.xml"""
        return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<idPkg:Fonts xmlns:idPkg="http://ns.adobe.com/AdobeInDesign/idml/1.0/packaging" DOMVersion="20.4">
    <Font Self="Font/HarmonyOS%20Sans%20SC" 
          FontFamily="HarmonyOS Sans SC" 
          FontName="HarmonyOS Sans SC Regular" 
          FontStyle="Regular" />
    <Font Self="Font/Mulish" 
          FontFamily="Mulish" 
          FontName="Mulish Regular" 
          FontStyle="Regular" />
    <Font Self="Font/Adobe%20%E5%AE%8B%E4%BD%93%20Std" 
          FontFamily="Adobe 宋体 Std" 
          FontName="Adobe 宋体 Std L" 
          FontStyle="L" />
</idPkg:Fonts>
'''
    
    def _generate_preferences_xml(self):
        """生成 Resources/Preferences.xml"""
        return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<idPkg:Preferences xmlns:idPkg="http://ns.adobe.com/AdobeInDesign/idml/1.0/packaging" DOMVersion="20.4">
    <Preferences>
        <GeneralPreference AutomaticLinkOption="16" />
        <TypographicPreference HangingPunctuation="true" />
    </Preferences>
</idPkg:Preferences>
'''
    
    def _generate_story_xml(self, content, story_id):
        """生成 Stories/Story_*.xml"""
        story_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Story xmlns:idPkg="http://ns.adobe.com/AdobeInDesign/idml/1.0/packaging" 
       DOMVersion="20.4" 
       Self="{story_id}" 
       XMLContent="false">
'''
        
        for item in content:
            item_type = item.get("type", "paragraph")
            text = item.get("text", "")
            style = item.get("style", "$ID/[No paragraph style]")
            
            if item_type == "heading":
                story_xml += f'''    <ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/{style}">
        <Content>{text}</Content>
        <Br />
    </ParagraphStyleRange>
'''
            elif item_type == "paragraph":
                story_xml += f'''    <ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/{style}">
        <Content>{text}</Content>
        <Br />
    </ParagraphStyleRange>
'''
        
        story_xml += '''</Story>
'''
        return story_xml
    
    def _generate_spread_xml(self, story_id, spread_id):
        """生成 Spreads/Spread_*.xml"""
        width, height = self.page_sizes.get(self.page_size, self.page_sizes["A4"])
        
        return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<idPkg:Spread xmlns:idPkg="http://ns.adobe.com/AdobeInDesign/idml/1.0/packaging" DOMVersion="20.4">
    <Spread Self="{spread_id}" FlattenerOverride="Default" SpreadHidden="false" AllowPageShuffle="true" ItemTransform="1 0 0 1 0 0" ShowMasterItems="true" PageCount="1" BindingLocation="0" PageTransitionType="None" PageTransitionDirection="NotApplicable" PageTransitionDuration="Medium">
        <Page Self="{spread_id}p" AppliedAlternateLayout="ucf" LayoutRule="UseMaster" SnapshotBlendingMode="IgnoreLayoutSnapshots" OptionalPage="false" GeometricBounds="0 0 {height} {width}" ItemTransform="1 0 0 1 0 0" Name="1" AppliedTrapPreset="TrapPreset/$ID/kDefaultTrapStyleName" OverrideList="" TabOrder="" GridStartingPoint="TopOutside" UseMasterGrid="true">
            <Properties>
                <Descriptor type="list">
                    <ListItem type="string"></ListItem>
                    <ListItem type="enumeration">Arabic</ListItem>
                    <ListItem type="boolean">true</ListItem>
                    <ListItem type="boolean">false</ListItem>
                    <ListItem type="long">1</ListItem>
                    <ListItem type="long">1</ListItem>
                    <ListItem type="string"></ListItem>
                </Descriptor>
                <PageColor type="enumeration">UseMasterColor</PageColor>
            </Properties>
            <MarginPreference ColumnCount="1" ColumnGutter="14.173228346456694" Top="{self.margins['top']}" Bottom="{self.margins['bottom']}" Left="{self.margins['left']}" Right="{self.margins['right']}" ColumnDirection="Horizontal" />
        </Page>
        <TextFrame Self="{spread_id}tf" ParentStory="{story_id}" ContentType="TextType" ItemLayer="ud7" Locked="false" Visible="true" ItemTransform="1 0 0 1 {self.margins['left']} {self.margins['top']}">
            <Properties>
                <PathGeometry>
                    <GeometryPathType PathOpen="false">
                        <PathPointArray>
                            <PathPointType Anchor="0 0" LeftDirection="0 0" RightDirection="0 0" />
                            <PathPointType Anchor="0 {height - self.margins['top'] - self.margins['bottom']}" LeftDirection="0 {height - self.margins['top'] - self.margins['bottom']}" RightDirection="0 {height - self.margins['top'] - self.margins['bottom']}" />
                            <PathPointType Anchor="{width - self.margins['left'] - self.margins['right']} {height - self.margins['top'] - self.margins['bottom']}" LeftDirection="{width - self.margins['left'] - self.margins['right']} {height - self.margins['top'] - self.margins['bottom']}" RightDirection="{width - self.margins['left'] - self.margins['right']} {height - self.margins['top'] - self.margins['bottom']}" />
                            <PathPointType Anchor="{width - self.margins['left'] - self.margins['right']} 0" LeftDirection="{width - self.margins['left'] - self.margins['right']} 0" RightDirection="{width - self.margins['left'] - self.margins['right']} 0" />
                        </PathPointArray>
                    </GeometryPathType>
                </PathGeometry>
            </Properties>
        </TextFrame>
    </Spread>
</idPkg:Spread>
'''
    
    def save(self, output_path):
        """保存 IDML 文件"""
        # 创建 ZIP 文件
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as idml:
            # 1. mimetype (必须是第一个，不压缩)
            idml.writestr('mimetype', self._generate_mimetype(), compress_type=zipfile.ZIP_STORED)
            
            # 2. META-INF/container.xml
            idml.writestr('META-INF/container.xml', self._generate_container_xml())
            
            # 3. designmap.xml
            idml.writestr('designmap.xml', self._generate_designmap_xml())
            
            # 4. Resources/
            idml.writestr('Resources/Styles.xml', self._generate_styles_xml())
            idml.writestr('Resources/Fonts.xml', self._generate_fonts_xml())
            idml.writestr('Resources/Preferences.xml', self._generate_preferences_xml())
            
            # 5. Stories/
            for i, page_content in enumerate(self.pages):
                story_id = self._generate_id("Story_")
                story_xml = self._generate_story_xml(page_content, story_id)
                idml.writestr(f'Stories/{story_id}.xml', story_xml)
                self.stories.append(story_id)
            
            # 6. Spreads/
            for story_id in self.stories:
                spread_id = self._generate_id("Spread_")
                spread_xml = self._generate_spread_xml(story_id, spread_id)
                idml.writestr(f'Spreads/{spread_id}.xml', spread_xml)
                self.spreads.append(spread_id)
        
        print(f"✅ IDML 生成成功：{output_path}")
        return output_path


# 测试
if __name__ == "__main__":
    # 创建生成器
    generator = IDMLGenerator(
        document_name="IEC11kW_Bi-directional_DC_Wallbox_Use_Manual",
        page_size="A4",
        language="zh-CN"
    )
    
    # 添加样式
    generator.add_paragraph_style("正文", {
        "font": "HarmonyOS Sans SC",
        "size": 10,
        "leading": 18,
        "space_after": 0
    })
    
    generator.add_paragraph_style("大标题", {
        "font": "Mulish",
        "size": 15,
        "leading": 18,
        "space_after": 12
    })
    
    generator.add_paragraph_style("小标题", {
        "font": "HarmonyOS Sans SC",
        "size": 12,
        "leading": 14,
        "space_after": 6
    })
    
    # 添加页面内容
    generator.add_page([
        {"type": "heading", "text": "1. 产品概述", "style": "大标题"},
        {"type": "paragraph", "text": "IEC11kW 双向直流充电桩是一款高性能充电设备。", "style": "正文"},
        {"type": "heading", "text": "1.1 技术规格", "style": "小标题"},
        {"type": "paragraph", "text": "输入电压：380V AC ±10%", "style": "正文"},
        {"type": "paragraph", "text": "输出功率：11kW DC", "style": "正文"}
    ])
    
    # 保存
    generator.save("/root/.openclaw/workspace/test_output.idml")
    print("测试完成！")
