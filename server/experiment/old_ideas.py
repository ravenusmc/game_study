# Getting the metascore 
# metascore_elements = soup.find("div", class_="c-productScoreInfo_scoreNumber")
# metascore = metascore_elements.text.strip()

# Getting the userscore 
userscore_elements = soup.find_all("div", class_="c-siteReviewScore_background")
# print(userscore_elements)
# for element in userscore_elements:
#     print(element.text)
# user_score = userscore_elements.text.strip()
# print(user_score)
