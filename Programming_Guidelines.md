# 程式碼風格指南

## 目錄

1. [回傳值](#回傳值)

## 回傳值

- 使用**int**作為狀態回傳值
- 執行成功: `return 0`
- 執行失誤: `return -1`
  - 如果此函數需要以回傳值傳輸資料: `return None`
- 停止程式: `return 1`

## 錯誤訊息

- `[<package name>.<module name>/<function name>]`
