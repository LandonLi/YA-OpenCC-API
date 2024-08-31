# YA-OpenCC-API

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/LandonLi/YA-OpenCC-API/docker-image.yaml)
![Docker Image Size (tag)](https://img.shields.io/docker/image-size/1andonli/ya-opencc-api/latest)
![Docker Pulls](https://img.shields.io/docker/pulls/1andonli/ya-opencc-api)

Yet another OpenCC API server.

This is a Python port of the [OpenCC.henry.wang](https://github.com/HenryQW/OpenCC.henry.wang) project.

## Install

```bash
wget https://cdn.jsdelivr.net/gh/LandonLi/YA-OpenCC-API@master/docker-compose.yaml
docker compose up -d
```

## Usage

### Conversions

There are 10 conversion schemes available in OpenCC:

- `s2t`: Simplified Chinese to Traditional Chinese 简体到繁体
- `t2s`: Traditional Chinese to Simplified Chinese 繁体到简体
- `s2tw`: Simplified Chinese to Traditional Chinese (Taiwan Standard) 简体到台湾正体
- `tw2s`: Traditional Chinese (Taiwan Standard) to Simplified Chinese 台湾正体到简体
- `s2hk`: Simplified Chinese to Traditional Chinese (Hong Kong Standard) 简体到香港繁体（香港小学学习字词表标准）
- `hk2s`: Traditional Chinese (Hong Kong Standard) to Simplified Chinese 香港繁体（香港小学学习字词表标准）到简体
- `s2twp`: Simplified Chinese to Traditional Chinese (Taiwan Standard) with Taiwanese idiom 简体到繁体（台湾正体标准）并转换爲台湾常用词彙
- `tw2sp`: Traditional Chinese (Taiwan Standard) to Simplified Chinese with Mainland Chinese idiom 繁体（台湾正体标准）到简体并转换爲中国大陆常用词彙
- `t2tw`: Traditional Chinese (OpenCC Standard) to Taiwan Standard 繁体（OpenCC 标准）到台湾正体
- `t2hk`: Traditional Chinese (OpenCC Standard) to Hong Kong Standard 繁体（OpenCC 标准）到香港繁体（香港小学学习字词表标准）

In order to use `t2hk`, the address you post to should be `http://localhost:5000/t2hk`.

Conversion scheme `t2s` will be used if you don't specify any.

### Params

1. `title`, text to convert, optional
2. `content`, text to convert, optional

### Example

```bash
curl --request POST \
  --url http://localhost:5000/t2s \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data 'title=繁體中文（中國大陸、澳門、馬新常稱繁體中文，台灣常稱正體中文或繁體中文）\
          &content=實際上，兩岸三地的繁體中文出版物並不拘泥於本地標準，有時使用其他字形和異體字是很頻繁的。'
```
