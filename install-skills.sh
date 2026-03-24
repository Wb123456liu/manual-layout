#!/bin/bash
# 安装技能脚本
# 用法: ./install-skills.sh

SKILLS=(
  "agent-browser"
  "browser-use"
  "desktop-control"
  "word-processor"
  "pdf-editor"
  "pdf-generator"
  "html-to-pdf"
  "document-ocr"
  "image-extract"
  "manual-typesetting"
  "manual-translation"
  "image"
  "imagemagick"
  "miaoda-image-understanding"
  "miaoda-text-gen-image"
  "chart-generator"
  "typescript-pro"
  "ecto-migrator"
  "self-improving-agent"
  "lecture-notes-master"
  "find-skills"
  "skill-vetter"
  "ontology"
  "miaoda-web-search"
  "miaoda-web-fetch"
  "miaoda-doc-parse"
  "miaoda-speech-to-text"
  "ui-ux-pro-max"
)

cd /root/.openclaw/workspace/skills

for skill in "${SKILLS[@]}"; do
  echo "=== Installing $skill ==="
  clawhub install "$skill" --force
  sleep 60  # 等待 60 秒避免 rate limit
done

echo "=== Done! ==="