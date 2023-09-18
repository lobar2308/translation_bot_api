import requests


def translate_api(text, from_lang, to_lang):

	url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

	payload = {
		"q": text,
		"target": to_lang,
		"source": from_lang
	}
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"Accept-Encoding": "application/gzip",
		"X-RapidAPI-Key": "ed11250849msh30f749d0458fe0ep1e8d66jsn55d444a40721",
		"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
	}

	response = requests.post(url, data=payload, headers=headers)

	return response.json()["data"]["translations"][0]["translatedText"]


# print(translate_api("apple", "en", "ru"))


