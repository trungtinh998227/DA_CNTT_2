"""
To get parallel en_vn language we should:
    1. Use english word from english words folder
    2. Each word, add this to the end of baseURL -> get all of example sentences of this page
    3. Add paging to get more example sentences (1->5 page is enough)
"""
baseURL = "https://glosbe.com/en/vi/"
paging = "?page=+2&tmmode=MUST" # phân trang
