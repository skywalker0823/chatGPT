# Simple ChatGPT example with LINE Messaging API

OpenAI官方chatGPT APP出來囉~關閉了

為了能更簡單的使用 chatGPT for LINE, 本專案會引導你/妳如何建置自己的 LineBot!
# Requirements
## About KEYs
### OpenAI API KEY
* OPENAI_API_KEY - https://platform.openai.com/account/api-keys
* 注意這個東西是要收費的，但是有免費的額度，可以先試試看。基本上 Pay as you go 如果你/妳不是大量使用的話，應該不會花太多錢。
* 這個 KEY 會用來跟 OpenAI 的 API 溝通，請務必保管好，不要上傳到 github 等公開的地方。
### LINE Messaging API KEYs
* LINE_CHANNEL_ACCESS_TOKEN
* LINE_CHANNEL_SECRET

# Deploy
## 本地端測試 - ngrok
## 部署 - EC2/Compute Engine 或其他雲服務的 VM
* 若有自己的VM也可以嘗試部署

## 部署 - Cloud Run
* 最推薦的方式，每個月若正常用量也不會花很多錢。

## 部署 - Vercel
* vercel 免費版(Hobby plan)有限制 timeout 10秒, 10秒對於chatgpt來說根本沒辦法進行什麼對話, 所以不建議使用 vercel 部署(除非你的小卡準備好了)。
