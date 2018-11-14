file_name = "sonar_data.txt"
file = open(file_name)

inputs = []
outputs = []


# Separate sonar_data.txt into its input data, and classification. 
for line in file:
	split_line = line.split(",")
	inputs += [[float(n) for n in split_line[:-1]] + [1]]
	print inputs
	outputs += [float(split_line[-1])]

w = [0.5 for i in range(len(inputs[0]))]


def predict(ins):
	return_me = 0

	for x in range(0, len(ins)):
		return_me += ins[x] * w[x]
		

	# return_me = sum([ins[x]*w[x] for x in range(len(ins))])

	if return_me > 0:
		return 1
	else:
		return 0

def train(ins, outs):

	global w

	error = outs - predict(ins)

	for x in xrange(len(w)):
		w[x] += error*0.0002*ins[x]


for i in xrange(10000000000):
	train(inputs[i%len(inputs)], outputs[i%len(outputs)])

	if i % 10000 == 0:
		print predict([0.0200,0.0371,0.0428,0.0207,0.0954,0.0986,0.1539,0.1601,0.3109,0.2111,0.1609,0.1582,0.2238,0.0645,0.0660,0.2273,0.3100,0.2999,0.5078,0.4797,0.5783,0.5071,0.4328,0.5550,0.6711,0.6415,0.7104,0.8080,0.6791,0.3857,0.1307,0.2604,0.5121,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,0.0510,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.0180,0.0084,0.0090,0.0032])# 1
		print predict([0.0317,0.0956,0.1321,0.1408,0.1674,0.1710,0.0731,0.1401,0.2083,0.3513,0.1786,0.0658,0.0513,0.3752,0.5419,0.5440,0.5150,0.4262,0.2024,0.4233,0.7723,0.9735,0.9390,0.5559,0.5268,0.6826,0.5713,0.5429,0.2177,0.2149,0.5811,0.6323,0.2965,0.1873,0.2969,0.5163,0.6153,0.4283,0.5479,0.6133,0.5017,0.2377,0.1957,0.1749,0.1304,0.0597,0.1124,0.1047,0.0507,0.0159,0.0195,0.0201,0.0248,0.0131,0.0070,0.0138,0.0092,0.0143,0.0036,0.0103])# 1
		print predict([0.0262,0.0582,0.1099,0.1083,0.0974,0.2280,0.2431,0.3771,0.5598,0.6194,0.6333,0.7060,0.5544,0.5320,0.6479,0.6931,0.6759,0.7551,0.8929,0.8619,0.7974,0.6737,0.4293,0.3648,0.5331,0.2413,0.5070,0.8533,0.6036,0.8514,0.8512,0.5045,0.1862,0.2709,0.4232,0.3043,0.6116,0.6756,0.5375,0.4719,0.4647,0.2587,0.2129,0.2222,0.2111,0.0176,0.1348,0.0744,0.0130,0.0106,0.0033,0.0232,0.0166,0.0095,0.0180,0.0244,0.0316,0.0164,0.0095,0.0078])# 1
		print predict([0.0211,0.0319,0.0415,0.0286,0.0121,0.0438,0.1299,0.1390,0.0695,0.0568,0.0869,0.1935,0.1478,0.1871,0.1994,0.3283,0.6861,0.5814,0.2500,0.1734,0.3363,0.5588,0.6592,0.7012,0.8099,0.8901,0.8745,0.7887,0.8725,0.9376,0.8920,0.7508,0.6832,0.7610,0.9017,1.0000,0.9123,0.7388,0.5915,0.4057,0.3019,0.2331,0.2931,0.2298,0.2391,0.1910,0.1096,0.0300,0.0171,0.0383,0.0053,0.0090,0.0042,0.0153,0.0106,0.0020,0.0105,0.0049,0.0070,0.0080])# 1
		print ""
		print predict([0.0210,0.0121,0.0203,0.1036,0.1675,0.0418,0.0723,0.0828,0.0494,0.0686,0.1125,0.1741,0.2710,0.3087,0.3575,0.4998,0.6011,0.6470,0.8067,0.9008,0.8906,0.9338,1.0000,0.9102,0.8496,0.7867,0.7688,0.7718,0.6268,0.4301,0.2077,0.1198,0.1660,0.2618,0.3862,0.3958,0.3248,0.2302,0.3250,0.4022,0.4344,0.4008,0.3370,0.2518,0.2101,0.1181,0.1150,0.0550,0.0293,0.0183,0.0104,0.0117,0.0101,0.0061,0.0031,0.0099,0.0080,0.0107,0.0161,0.0133])# 0
		print predict([0.0454,0.0472,0.0697,0.1021,0.1397,0.1493,0.1487,0.0771,0.1171,0.1675,0.2799,0.3323,0.4012,0.4296,0.5350,0.5411,0.6870,0.8045,0.9194,0.9169,1.0000,0.9972,0.9093,0.7918,0.6705,0.5324,0.3572,0.2484,0.3161,0.3775,0.3138,0.1713,0.2937,0.5234,0.5926,0.5437,0.4516,0.3379,0.3215,0.2178,0.1674,0.2634,0.2980,0.2037,0.1155,0.0919,0.0882,0.0228,0.0380,0.0142,0.0137,0.0120,0.0042,0.0238,0.0129,0.0084,0.0218,0.0321,0.0154,0.0053])# 0
		print predict([0.0303,0.0353,0.0490,0.0608,0.0167,0.1354,0.1465,0.1123,0.1945,0.2354,0.2898,0.2812,0.1578,0.0273,0.0673,0.1444,0.2070,0.2645,0.2828,0.4293,0.5685,0.6990,0.7246,0.7622,0.9242,1.0000,0.9979,0.8297,0.7032,0.7141,0.6893,0.4961,0.2584,0.0969,0.0776,0.0364,0.1572,0.1823,0.1349,0.0849,0.0492,0.1367,0.1552,0.1548,0.1319,0.0985,0.1258,0.0954,0.0489,0.0241,0.0042,0.0086,0.0046,0.0126,0.0036,0.0035,0.0034,0.0079,0.0036,0.0048])# 0
		print predict([0.0260,0.0363,0.0136,0.0272,0.0214,0.0338,0.0655,0.1400,0.1843,0.2354,0.2720,0.2442,0.1665,0.0336,0.1302,0.1708,0.2177,0.3175,0.3714,0.4552,0.5700,0.7397,0.8062,0.8837,0.9432,1.0000,0.9375,0.7603,0.7123,0.8358,0.7622,0.4567,0.1715,0.1549,0.1641,0.1869,0.2655,0.1713,0.0959,0.0768,0.0847,0.2076,0.2505,0.1862,0.1439,0.1470,0.0991,0.0041,0.0154,0.0116,0.0181,0.0146,0.0129,0.0047,0.0039,0.0061,0.0040,0.0036,0.0061,0.0115])# 0
		print ""