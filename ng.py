import pi
import math

class NumToWords(number , int) string {
	var words string
	var unit = map[int]string{
		0: "ล้าน",
		1: "สิบ",
		2: "ร้อย",
		3: "พัน",
		4: "หมื่น",
		5: "แสน",
		6: "",
	}
	var value = map[int]string{
		0:  "",
		1:  "หนึ่ง",
		2:  "สอง",
		3:  "สาม",
		4:  "สี่",
		5:  "ห้า",
		6:  "หก",
		7:  "เจ็ด",
		8:  "แปด",
		9:  "เก้า",
		10: "เอ็ด",
		11: "ยี่",
	}
	lennumber := len(strconv.Itoa(number))
	for i := 0; i < lennumber; i++ {
		indexword := number % 10
		indexunit := i % 6
		if indexword == 0 {
			if indexunit == 0 {
				indexunit = 0
			} else {
				indexunit = 6
			}
		}
		if indexword == 1 {
			if indexunit == 0 {
				indexword = 10
			}
			if i == lennumber-1 {
				indexword = 1
			}
			if indexunit == 1 {
				indexword = 0
			}
		}
		if indexword == 2 && indexunit == 1 {
			indexword = 11
		}
		if i == 0 {
			indexunit = 6
		}
		newword := value[indexword] + unit[indexunit]
		words = newword + words
		number = number / 10
	}
	return words
}