from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, WebBaseLoader

url = "https://www.flipkart.com/samsung-m7-series-107-9-cm-43-inch-4k-ultra-hd-led-backlit-va-panel-in-built-speaker-smart-tv-apps-airplay-wi-fi-bluetooth-usb-type-c-wireless-display-vision-ai-monitor-ls43fm700uwxxl/p/itm3d915c6583e0d?pid=MONHDA8MQBMRZVCH&lid=LSTMONHDA8MQBMRZVCHVVK4M4&marketplace=FLIPKART&store=6bo%2Fg0i%2F9no&srno=b_1_1&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&fm=organic&iid=en_QqzEeHZbPFkemVbsrBGmLIRYcpt5c6t8RkuwUxPELB8k09JkjaQQRIY_VnQeKbxPbl2CBfejXb6WZd2drrugkg%3D%3D&ppt=hp&ppn=homepage&ssid=pbynw79g1c0000001768285370507"

loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)