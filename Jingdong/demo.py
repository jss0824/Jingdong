import requests
import json
import re
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
# }
# url = 'https://club.jd.com/comment/productPageComments.action?'
#
# data = {
#     'callback':'fetchJSON_comment98',
#     'productId':'10632536214',
#     'score':'0',
#     'sortType':'5',
#     'page':'1',
#     'pageSize':'10',
#     'isShadowSku':'0',
#     'rid':'0',
#     'fold':'1'
# }
#
# res = requests.get(url, params=data, headers=headers).text
#
#
# data = re.findall(r'fetchJSON_comment98\((.*)\)',res)
# print(data)


str = {
	"productAttr": [{
		"unit": "厘米",
		"name": "身高",
		"type": "people_height",
		"key": "firstAttribute"
	}, {
		"unit": "公斤",
		"name": "体重",
		"type": "people_weight",
		"key": "secondAttribute"
	}],
	"productCommentSummary": {
		"skuId": 67407055547,
		"averageScore": 5,
		"defaultGoodCount": 147,
		"defaultGoodCountStr": "100+",
		"commentCount": 252,
		"commentCountStr": "200+",
		"goodCount": 105,
		"goodCountStr": "100+",
		"goodRate": 1.0,
		"goodRateShow": 100,
		"generalCount": 0,
		"generalCountStr": "0",
		"generalRate": 0.0,
		"generalRateShow": 0,
		"poorCount": 0,
		"poorCountStr": "0",
		"poorRate": 0.0,
		"poorRateShow": 0,
		"videoCount": 0,
		"videoCountStr": "0",
		"afterCount": 0,
		"afterCountStr": "0",
		"showCount": 0,
		"showCountStr": "0",
		"oneYear": 0,
		"sensitiveBook": 0,
		"fixCount": 0,
		"plusCount": 0,
		"plusCountStr": "0",
		"buyerShow": 0,
		"poorRateStyle": 0,
		"generalRateStyle": 0,
		"goodRateStyle": 150,
		"installRate": 0,
		"productId": 67407055547,
		"score1Count": 0,
		"score2Count": 0,
		"score3Count": 0,
		"score4Count": 0,
		"score5Count": 105
	},
	"hotCommentTagStatistics": [],
	"jwotestProduct": null,
	"maxPage": 7,
	"testId": "cmt",
	"score": 0,
	"soType": 5,
	"imageListCount": 0,
	"vTagStatistics": null,
	"csv": "eid=100^^tagid=ALL^^pid=20003^^sku=14331700595^^sversion=1001^^pageSize=1",
	"comments": [{
		"id": 14051921397,
		"guid": "6f7fed02-ea95-4588-8bf3-43718178f3e3",
		"content": "裙子收到了，跟图片这样是一样的正品，质量很不错，大小很合适，穿着很舒适有气质。",
		"creationTime": "2020-04-19 10:54:14",
		"isDelete": false,
		"isTop": false,
		"userImageUrl": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"topped": 0,
		"replyCount": 0,
		"score": 5,
		"title": "",
		"usefulVoteCount": 0,
		"userClient": 22,
		"anonymousFlag": 0,
		"plusAvailable": 0,
		"mobileVersion": "",
		"productColor": "图片色",
		"productSize": "M",
		"textIntegral": 10,
		"status": 1,
		"referenceId": "67279058586",
		"referenceTime": "2020-04-17 13:16:45",
		"nickname": "w***g",
		"replyCount2": 0,
		"userImage": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"orderId": 0,
		"integral": 10,
		"productSales": "[]",
		"referenceImage": "jfs/t1/93263/26/17331/142581/5e854624E243e52fa/25e5a66db8615aa8.jpg",
		"referenceName": "花颜绘雪纺连衣裙女2020春夏季新款女装时尚蕾丝印碎花连衣裙子 粉色 XL",
		"firstCategory": 1315,
		"secondCategory": 1343,
		"thirdCategory": 9719,
		"aesPin": "AH9PnXbMdREZXzZBNcbYMoEFzawonbD1ATdEXPDkWkKIzA5AP4F426AyUCf7E6ESGV86RqYkxpSifLmdF_rLIw",
		"days": 2,
		"afterDays": 0
	}, {
		"id": 14051924763,
		"guid": "d14bfd4d-3e20-4160-8e78-2cb7a3ce64af",
		"content": "很合身质量不错，大小很合适，线条处理得很，干净好姐妹都问我要链接。",
		"creationTime": "2020-04-19 10:54:54",
		"isDelete": false,
		"isTop": false,
		"userImageUrl": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"topped": 0,
		"replyCount": 0,
		"score": 5,
		"title": "",
		"usefulVoteCount": 0,
		"userClient": 22,
		"anonymousFlag": 0,
		"plusAvailable": 0,
		"mobileVersion": "",
		"productColor": "图片色",
		"productSize": "M",
		"textIntegral": 10,
		"status": 1,
		"referenceId": "67279058586",
		"referenceTime": "2020-04-17 13:16:44",
		"nickname": "w***K",
		"replyCount2": 0,
		"userImage": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"orderId": 0,
		"integral": 10,
		"productSales": "[]",
		"referenceImage": "jfs/t1/93263/26/17331/142581/5e854624E243e52fa/25e5a66db8615aa8.jpg",
		"referenceName": "花颜绘雪纺连衣裙女2020春夏季新款女装时尚蕾丝印碎花连衣裙子 粉色 XL",
		"firstCategory": 1315,
		"secondCategory": 1343,
		"thirdCategory": 9719,
		"aesPin": "fN4bsE6RFF_o3CylHO9j5VOkNhbvPlDlA-t7yNtcDAg2w3jl6bxblTIHW4Sa3LHUbqfAQWN4X4RKLL1qCidejQ",
		"days": 2,
		"afterDays": 0
	}, {
		"id": 14024679142,
		"guid": "c099fdf5-1342-425b-8df4-70ee8ef140c9",
		"content": "裙子超级好看的，用料讲究，做工精细，没有多余的线头。",
		"creationTime": "2020-04-12 11:04:17",
		"isDelete": false,
		"isTop": false,
		"userImageUrl": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"topped": 0,
		"replyCount": 0,
		"score": 5,
		"title": "",
		"usefulVoteCount": 2,
		"userClient": 22,
		"anonymousFlag": 0,
		"plusAvailable": 0,
		"mobileVersion": "",
		"productColor": "图片色",
		"productSize": "M",
		"textIntegral": 20,
		"status": 1,
		"referenceId": "67279058586",
		"referenceTime": "2020-04-10 13:55:57",
		"nickname": "w***k",
		"replyCount2": 0,
		"userImage": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"orderId": 0,
		"integral": 20,
		"productSales": "[]",
		"referenceImage": "jfs/t1/93263/26/17331/142581/5e854624E243e52fa/25e5a66db8615aa8.jpg",
		"referenceName": "花颜绘雪纺连衣裙女2020春夏季新款女装时尚蕾丝印碎花连衣裙子 粉色 XL",
		"firstCategory": 1315,
		"secondCategory": 1343,
		"thirdCategory": 9719,
		"aesPin": "aL75HbpI9quX6xVKTSaV6W5xbfSdSHxStITx0fO2fbPANyCaw-z6lo5rONUpjkZ36qK6EgWcwL0ErqxVN_jm9A",
		"days": 2,
		"afterDays": 0
	}, {
		"id": 14048703434,
		"guid": "37c53b1b-7116-43d6-915f-d1e20dcf4f18",
		"content": "衣服收到了，质量非常不错，穿上去很好看，我很喜欢这个颜色，我最喜欢了，谢谢店家。",
		"creationTime": "2020-04-18 14:18:21",
		"isDelete": false,
		"isTop": false,
		"userImageUrl": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"topped": 0,
		"replyCount": 0,
		"score": 5,
		"title": "",
		"usefulVoteCount": 0,
		"userClient": 22,
		"anonymousFlag": 0,
		"plusAvailable": 0,
		"mobileVersion": "",
		"productColor": "图片色",
		"productSize": "M",
		"textIntegral": 20,
		"status": 1,
		"referenceId": "67279058586",
		"referenceTime": "2020-04-16 14:47:07",
		"nickname": "EtbSIYPGqzVf",
		"replyCount2": 0,
		"userImage": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"orderId": 0,
		"integral": 20,
		"productSales": "[]",
		"referenceImage": "jfs/t1/93263/26/17331/142581/5e854624E243e52fa/25e5a66db8615aa8.jpg",
		"referenceName": "花颜绘雪纺连衣裙女2020春夏季新款女装时尚蕾丝印碎花连衣裙子 粉色 XL",
		"firstCategory": 1315,
		"secondCategory": 1343,
		"thirdCategory": 9719,
		"aesPin": "Fk1oeq3JEaPTa6si0NcJXvD_TYZsfiNHKfjTqtwvRq-wcS-h18Vggfs1LjcUb1dx-B_qLU_z1DDhcPaWBOkiIg",
		"days": 2,
		"afterDays": 0
	}, {
		"id": 14028323877,
		"guid": "b31a103c-d069-4a48-8c86-41757885b4d0",
		"content": "质量很好，真的很不错，跟图片上的一样一样的，尺码也很标准，包装非常好",
		"creationTime": "2020-04-13 10:29:03",
		"isDelete": false,
		"isTop": false,
		"userImageUrl": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"topped": 0,
		"replyCount": 0,
		"score": 5,
		"title": "",
		"usefulVoteCount": 0,
		"userClient": 22,
		"anonymousFlag": 0,
		"plusAvailable": 0,
		"mobileVersion": "",
		"productColor": "图片色",
		"productSize": "M",
		"textIntegral": 20,
		"status": 1,
		"referenceId": "67279058586",
		"referenceTime": "2020-04-11 16:20:22",
		"nickname": "w***X",
		"replyCount2": 0,
		"userImage": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"orderId": 0,
		"integral": 20,
		"productSales": "[]",
		"referenceImage": "jfs/t1/93263/26/17331/142581/5e854624E243e52fa/25e5a66db8615aa8.jpg",
		"referenceName": "花颜绘雪纺连衣裙女2020春夏季新款女装时尚蕾丝印碎花连衣裙子 粉色 XL",
		"firstCategory": 1315,
		"secondCategory": 1343,
		"thirdCategory": 9719,
		"aesPin": "gBxjIZI-am7uMEHPHsRNQI3T1SEULDDkrtIYvHDzP0p7x_SCBR9Qc7i_YiASUwy_gSGoixoHoPcsOZ7FIT3VUQ",
		"days": 2,
		"afterDays": 0
	}, {
		"id": 14048670039,
		"guid": "1b2f7ae8-fb2f-4ba9-9b8c-60e29f1de55f",
		"content": "衣服收到了，试穿了，感觉效果不错穿上去很好看男朋友很喜欢，下次还来买。",
		"creationTime": "2020-04-18 14:10:20",
		"isDelete": false,
		"isTop": false,
		"userImageUrl": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"topped": 0,
		"replyCount": 0,
		"score": 5,
		"title": "",
		"usefulVoteCount": 0,
		"userClient": 22,
		"anonymousFlag": 0,
		"plusAvailable": 0,
		"mobileVersion": "",
		"productColor": "图片色",
		"productSize": "M",
		"textIntegral": 20,
		"status": 1,
		"referenceId": "67279058586",
		"referenceTime": "2020-04-16 14:36:44",
		"nickname": "w***A",
		"replyCount2": 0,
		"userImage": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"orderId": 0,
		"integral": 20,
		"productSales": "[]",
		"referenceImage": "jfs/t1/93263/26/17331/142581/5e854624E243e52fa/25e5a66db8615aa8.jpg",
		"referenceName": "花颜绘雪纺连衣裙女2020春夏季新款女装时尚蕾丝印碎花连衣裙子 粉色 XL",
		"firstCategory": 1315,
		"secondCategory": 1343,
		"thirdCategory": 9719,
		"aesPin": "sNVUHD2VerpKMlmSyXs2tONiR0MElzeKl1y3Ij_XeVQVrZ9SzvIata0fMzyw_g03lctMiZuhCK5PJebHq7pAdg",
		"days": 2,
		"afterDays": 0
	}, {
		"id": 14028331191,
		"guid": "49d98c21-ced3-4d4c-ab1d-f37abdd7adb8",
		"content": "质量很好，真的很不错，跟图片上的一样，无色差，尺码也很标准，满意",
		"creationTime": "2020-04-13 10:30:40",
		"isDelete": false,
		"isTop": false,
		"userImageUrl": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"topped": 0,
		"replyCount": 0,
		"score": 5,
		"title": "",
		"usefulVoteCount": 0,
		"userClient": 22,
		"anonymousFlag": 0,
		"plusAvailable": 0,
		"mobileVersion": "",
		"productColor": "图片色",
		"productSize": "M",
		"textIntegral": 20,
		"status": 1,
		"referenceId": "67279058586",
		"referenceTime": "2020-04-11 16:24:20",
		"nickname": "w***P",
		"replyCount2": 0,
		"userImage": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"orderId": 0,
		"integral": 20,
		"productSales": "[]",
		"referenceImage": "jfs/t1/93263/26/17331/142581/5e854624E243e52fa/25e5a66db8615aa8.jpg",
		"referenceName": "花颜绘雪纺连衣裙女2020春夏季新款女装时尚蕾丝印碎花连衣裙子 粉色 XL",
		"firstCategory": 1315,
		"secondCategory": 1343,
		"thirdCategory": 9719,
		"aesPin": "IiE2YcrJGdspP4Jzt9LA0gzCyRHTzqqNLmWjG-93hHPXlaNaIl81PYWdWPTaPDAYX65IZEaNEB7iwlJzbTdxzA",
		"days": 2,
		"afterDays": 0
	}, {
		"id": 14048675648,
		"guid": "180ea1bf-9985-4ed4-a220-8e8b81f7a0df",
		"content": "哈哈哈哈宝贝是真的不错无所超值很满意的一次网购感觉穿上去很好看，朋友都要链接。",
		"creationTime": "2020-04-18 14:11:41",
		"isDelete": false,
		"isTop": false,
		"userImageUrl": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"topped": 0,
		"replyCount": 0,
		"score": 5,
		"title": "",
		"usefulVoteCount": 0,
		"userClient": 22,
		"anonymousFlag": 0,
		"plusAvailable": 0,
		"mobileVersion": "",
		"productColor": "图片色",
		"productSize": "M",
		"textIntegral": 10,
		"status": 1,
		"referenceId": "67279058586",
		"referenceTime": "2020-04-16 14:37:58",
		"nickname": "w***O",
		"replyCount2": 0,
		"userImage": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"orderId": 0,
		"integral": 10,
		"productSales": "[]",
		"referenceImage": "jfs/t1/93263/26/17331/142581/5e854624E243e52fa/25e5a66db8615aa8.jpg",
		"referenceName": "花颜绘雪纺连衣裙女2020春夏季新款女装时尚蕾丝印碎花连衣裙子 粉色 XL",
		"firstCategory": 1315,
		"secondCategory": 1343,
		"thirdCategory": 9719,
		"aesPin": "nik7RAmUYzo5n9E1HutYYvYHlHBAQVWjZKcdJtlf21TFrv82MUb6qWoEfokZm27OKam6dIVxdCdd0iIaxBM71g",
		"days": 2,
		"afterDays": 0
	}, {
		"id": 14037014514,
		"guid": "991fda2e-a907-4ab0-ae21-dca9111e6c57",
		"content": "非常好非常棒，就是高端大气上档次，低调奢华有内涵的感觉。",
		"creationTime": "2020-04-15 14:16:37",
		"isDelete": false,
		"isTop": false,
		"userImageUrl": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"topped": 0,
		"replyCount": 0,
		"score": 5,
		"title": "",
		"usefulVoteCount": 1,
		"userClient": 22,
		"anonymousFlag": 0,
		"plusAvailable": 0,
		"mobileVersion": "",
		"productColor": "图片色",
		"productSize": "M",
		"textIntegral": 20,
		"status": 1,
		"referenceId": "67279058586",
		"referenceTime": "2020-04-13 14:10:55",
		"nickname": "w***C",
		"replyCount2": 0,
		"userImage": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"orderId": 0,
		"integral": 20,
		"productSales": "[]",
		"referenceImage": "jfs/t1/93263/26/17331/142581/5e854624E243e52fa/25e5a66db8615aa8.jpg",
		"referenceName": "花颜绘雪纺连衣裙女2020春夏季新款女装时尚蕾丝印碎花连衣裙子 粉色 XL",
		"firstCategory": 1315,
		"secondCategory": 1343,
		"thirdCategory": 9719,
		"aesPin": "KEz2wT2M08B48g4PhRgJgF_Oo3CxFLE2_iVLvbr7Raz8c2s5TAWc7Mwc8Xn-BmNZ3W9_7LGILncp0L5sZ57dZA",
		"days": 2,
		"afterDays": 0
	}, {
		"id": 14051842388,
		"guid": "f74dd2d0-7817-4f76-9a3a-c4d5377e1914",
		"content": "质量很好，颜色没有色差，跟店家推荐的号码大小都合适。",
		"creationTime": "2020-04-19 10:36:39",
		"isDelete": false,
		"isTop": false,
		"userImageUrl": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"topped": 0,
		"replyCount": 0,
		"score": 5,
		"title": "",
		"usefulVoteCount": 0,
		"userClient": 22,
		"anonymousFlag": 0,
		"plusAvailable": 0,
		"mobileVersion": "",
		"productColor": "图片色",
		"productSize": "M",
		"textIntegral": 10,
		"status": 1,
		"referenceId": "67279058586",
		"referenceTime": "2020-04-17 12:05:19",
		"nickname": "w***o",
		"replyCount2": 0,
		"userImage": "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
		"orderId": 0,
		"integral": 10,
		"productSales": "[]",
		"referenceImage": "jfs/t1/93263/26/17331/142581/5e854624E243e52fa/25e5a66db8615aa8.jpg",
		"referenceName": "花颜绘雪纺连衣裙女2020春夏季新款女装时尚蕾丝印碎花连衣裙子 粉色 XL",
		"firstCategory": 1315,
		"secondCategory": 1343,
		"thirdCategory": 9719,
		"aesPin": "V_kRcqqAb3s7s-1QBzHXlI1bDuaRqDMiKdzOzqTMeoZPeGAUPtjRnUrq2R-1kDu-GO6WnJwOgFqbruPT6k8FMg",
		"days": 2,
		"afterDays": 0
	}]
}
import re
data = re.sub('null','',str)
comment = data['productCommentSummary']
print(comment)