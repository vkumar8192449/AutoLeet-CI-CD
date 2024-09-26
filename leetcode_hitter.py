import requests

# Define the URL and the payload
url = "https://leetcode.com/problems/two-sum/submit/"
payload = {
    "lang": "cpp",
    "question_id": "1",
    "typed_code": """class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            
        }
};"""
}

# Define the headers
headers = {
    "authority": "leetcode.com",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,hi;q=0.8",
    "content-type": "application/json",
    "origin": "https://leetcode.com",
    "referer": "https://leetcode.com/problems/two-sum/submissions/1402595395/",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36",
    "x-csrftoken": "qIdZRYc9JjcvGyUGvWs99NwqyJJq8f0vWM98qBzKGFC3EmeS4fyDpk7CBQTY8dik",
    "cookie": """gr_user_id=e056cee0-b555-4682-934d-457df9a6bb1d; __stripe_mid=b7d98694-a622-40d9-bd12-d5e8055bd8d5da5dc2; 87b5a3c3f1a55520_gr_last_sent_cs1=vkumar8192449; _ga_DKXQ03QCVK=GS1.1.1694192424.1.1.1694192427.57.0.0; __gads=ID=3afb41e811ecaa2d:T=1704272548:RT=1718180668:S=ALNI_MYnfkkLUJjNDuY4KCYJtMSFTDJ9iw; __gpi=UID=00000cd09949cd1d:T=1704272548:RT=1718180668:S=ALNI_Ma5ZrveGlF9_hRcReJeOgcl2eNpVQ; FCCDCF=%5Bnull%2Cnull%2Cnull%2C%5B%22CQAGPIAQAGPIAEsACBENA4EgAAAAAEPgACiQAAAOhQD2F2K2kKFkPCmQWYAQBCijYEAhQAAAAkCBIAAgAUgQAgFIIAgAIFAAAAAAAAAQEgCQAAQABAAAIACgAAAAAAIAAAAAAAQQAAAAAIAAAAAAAAEAAAAAAAQAAAAIAABEhCAAQQAEAAAAAAAQAAAAAAAAAAABAAA%22%2C%222~~dv.70.89.93.108.122.149.196.259.311.313.323.358.415.449.486.494.495.540.574.609.827.864.981.1029.1048.1051.1095.1097.1126.1205.1211.1276.1301.1365.1415.1423.1449.1570.1577.1598.1651.1716.1735.1753.1765.1870.1878.1889.1958.2072.2253.2299.2357.2373.2415.2506.2526.2568.2571.2575.2624.2677%22%2C%2281F1FEB2-FAAF-42C2-BD5E-D4448F337240%22%5D%5D; _ga_CDRWKZTDEX=deleted; INGRESSCOOKIE=0b0694770baca2bc8abe35886d6bcc6c|8e0876c7c1464cc0ac96bc2edceabd27; ip_check=(false, "202.168.87.79"); 87b5a3c3f1a55520_gr_session_id=2ef45946-27c8-420c-8813-80277f701e32; 87b5a3c3f1a55520_gr_last_sent_sid_with_cs1=2ef45946-27c8-420c-8813-80277f701e32; _gid=GA1.2.2030680657.1727329366; 87b5a3c3f1a55520_gr_session_id_sent_vst=2ef45946-27c8-420c-8813-80277f701e32; cf_clearance=j_NjaoQgsJXD0xJ6MvSMfRLVXzltdeYzmo4FdMFpZIE-1727329421-1.2.1.1-OQi0ZLpQEL3DtAIaKVIWWbgHaZDmwWmDJaB9A8EYFji373O5khCbjeOHFza09cIXDT92XT4A0JP5tir.jH4Aa8o9Cstqke0BfzpQVsHJiJ3j.KIJYj6U0PgiARax5C2gY9.cqOKWyhI6EVlSBuI9hZiRPUKQvLPJ1xPC6KchOIAOhv4Fcp9grQzV9tkhW7fmpHlhvi2TJH2_Mvy37mEtm4YMEcT29IsYqXdYRrAWQ31xjvwXDCZ7abdMaKif45fEkpgXshU52C2B.NTe4fdpYujO7wofEtsRB8wV9DtZWeNwSIcKs5z9jgaYVnkoMMHGXpRt9iMZosFtS09JXBLQelwZ_0hO28ACHTDeRGpZI9JoB0h312Mgsgq.bQymLf_7QbQY_Q7pHJSfJuUSUuAovCbnrb4c4tCqlN.z7xEhBP.3e24BXek1vD4Qr5T89zejWHJ9f7fiYaD700Wyu9FYHA; csrftoken=qIdZRYc9JjcvGyUGvWs99NwqyJJq8f0vWM98qBzKGFC3EmeS4fyDpk7CBQTY8dik; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgdmt1bWFyODE5MjQ0OS4iXV0:1sthHz:lEjhn5hlwDdQausrc-MY21_225tZlEgJrC05uSCjInw; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjY1NjM1MCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMzQ2ZGE5NWRmNzEyMGNkY2Q0YTM5NjRiOTdlNWZkZjVmOGNkY2RjODBjZGU2MDVlNDZhZmU5OGEwYjRlZWRiZiIsImlkIjoyNjU2MzUwLCJlbWFpbCI6InZrdW1hcjgxOTI0NDlAZ21haWwuY29tIiwidXNlcm5hbWUiOiJ2a3VtYXI4MTkyNDQ5IiwidXNlcl9zbHVnIjoidmt1bWFyODE5MjQ0OSIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9hdmF0YXJzL2F2YXRhcl8xNjczODcxMzEyLnBuZyIsInJlZnJlc2hlZF9hdCI6MTcyNzMyOTQyMiwiaXAiOiIyMDIuMTY4Ljg3Ljc5IiwiaWRlbnRpdHkiOiJiY2Y3MDNmOWJlYjU1NDkyNDFiOTRiYjY3ZjRlOWFjMCIsImRldmljZV93aXRoX2lwIjpbImYzNDFkZjdhNDY2Nzc5NTliNmMzYTU2ZDExZjA0ZWQ4IiwiMjAyLjE2OC44Ny43OSJdLCJzZXNzaW9uX2lkIjo3MzYyNzQ0NSwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.MFIZX-pdHU7f69YYobn08_a7R8H01m9A9MosFYsJ-cY; __eoi=ID=e5dce868f858eb0b:T=1722109906:RT=1727329439:S=AA-AfjYwjBzGc5E0JuSDOL3P2v8w; __cf_bm=jARxjIRvGfJ1uBMm56eoh5rNlYHcd8ExJI0GGdN4ZXE-1727329679-1.0.1.1-4kgByRVy4nIcVwWSiR29p1wiCJqMiFqiu6j_g2204pe7cJmtwjkvdwrSKyj8VUEvh8GQOI1CmwGH2rvtMruIXg; 87b5a3c3f1a55520_gr_cs1=vkumar8192449; _gat=1; _ga=GA1.1.1942175728.1706497737; _ga_CDRWKZTDEX=GS1.1.1727329365.394.1.1727329835.59.0.0"""
}

# Send the POST request
response = requests.post(url, json=payload, headers=headers)

# Print response
print(response.status_code)
print(response.json())
