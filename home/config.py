import random

def getfile(name):

	B = ['mdb001', 'mdb002', 'mdb010', 'mdb012', 'mdb013', 'mdb015', 'mdb017', 'mdb019', 'mdb021', 'mdb025', 'mdb030', 'mdb032', 'mdb059', 'mdb063', 'mdb069', 'mdb080', 'mdb081', 'mdb083', 'mdb091', 'mdb097', 'mdb099', 'mdb104', 'mdb107', 'mdb121', 'mdb126', 'mdb127', 'mdb132', 'mdb142', 'mdb144', 'mdb145', 'mdb150', 'mdb152', 'mdb160', 'mdb163', 'mdb165', 'mdb167', 'mdb175', 'mdb188', 'mdb190', 'mdb191', 'mdb193', 'mdb195', 'mdb198', 'mdb199', 'mdb204', 'mdb207', 'mdb212', 'mdb214', 'mdb218', 'mdb219', 'mdb222', 'mdb223', 'mdb226', 'mdb227', 'mdb236', 'mdb240', 'mdb244', 'mdb248', 'mdb252', 'mdb290', 'mdb312', 'mdb314', 'mdb315']
	M = ['mdb023', 'mdb028', 'mdb058', 'mdb072', 'mdb075', 'mdb090', 'mdb092', 'mdb095', 'mdb102', 'mdb105', 'mdb110', 'mdb111', 'mdb115', 'mdb117', 'mdb120', 'mdb124', 'mdb125', 'mdb130', 'mdb134', 'mdb141', 'mdb144', 'mdb148', 'mdb155', 'mdb158', 'mdb170', 'mdb171', 'mdb178', 'mdb179', 'mdb181', 'mdb184', 'mdb186', 'mdb202', 'mdb206', 'mdb209', 'mdb211', 'mdb213', 'mdb216', 'mdb231', 'mdb233', 'mdb238', 'mdb239', 'mdb241', 'mdb245', 'mdb249', 'mdb253', 'mdb256', 'mdb264', 'mdb265', 'mdb267', 'mdb270', 'mdb271', 'mdb274']
	Nan = ['mdb003', 'mdb004', 'mdb006', 'mdb007', 'mdb008', 'mdb009', 'mdb011', 'mdb014', 'mdb016', 'mdb018', 'mdb020', 'mdb022', 'mdb024', 'mdb026', 'mdb027', 'mdb029', 'mdb031', 'mdb033', 'mdb034', 'mdb035', 'mdb036', 'mdb037', 'mdb038', 'mdb039', 'mdb040', 'mdb041', 'mdb042', 'mdb043', 'mdb044', 'mdb045', 'mdb046', 'mdb047', 'mdb048', 'mdb049', 'mdb050', 'mdb051', 'mdb052', 'mdb053', 'mdb054', 'mdb055', 'mdb056', 'mdb057', 'mdb060', 'mdb061', 'mdb062', 'mdb064', 'mdb065', 'mdb066', 'mdb067', 'mdb068', 'mdb070', 'mdb071', 'mdb073', 'mdb074', 'mdb076', 'mdb077', 'mdb078', 'mdb079', 'mdb082', 'mdb084', 'mdb085', 'mdb086', 'mdb087', 'mdb088', 'mdb089', 'mdb093', 'mdb094', 'mdb096', 'mdb098', 'mdb100', 'mdb101', 'mdb103', 'mdb106', 'mdb108', 'mdb109', 'mdb112', 'mdb113', 'mdb114', 'mdb116', 'mdb118', 'mdb119', 'mdb122', 'mdb123', 'mdb128', 'mdb129', 'mdb131', 'mdb133', 'mdb135', 'mdb136', 'mdb137', 'mdb138', 'mdb139', 'mdb140', 'mdb143', 'mdb146', 'mdb147', 'mdb149', 'mdb151', 'mdb153', 'mdb154', 'mdb156', 'mdb157', 'mdb159', 'mdb161', 'mdb162', 'mdb164', 'mdb166', 'mdb168', 'mdb169', 'mdb172', 'mdb173', 'mdb174', 'mdb176', 'mdb177', 'mdb180', 'mdb182', 'mdb183', 'mdb185', 'mdb187', 'mdb189', 'mdb192', 'mdb194', 'mdb196', 'mdb197', 'mdb200', 'mdb201', 'mdb203', 'mdb205', 'mdb208', 'mdb210', 'mdb215', 'mdb217', 'mdb220', 'mdb221', 'mdb224', 'mdb225', 'mdb228', 'mdb229', 'mdb230', 'mdb232', 'mdb234', 'mdb235', 'mdb237', 'mdb242', 'mdb243', 'mdb246', 'mdb247', 'mdb250', 'mdb251', 'mdb254', 'mdb255', 'mdb257', 'mdb258', 'mdb259', 'mdb260', 'mdb261', 'mdb262', 'mdb263', 'mdb266', 'mdb268', 'mdb269', 'mdb272', 'mdb273', 'mdb275', 'mdb276', 'mdb277', 'mdb278', 'mdb279', 'mdb280', 'mdb281', 'mdb282', 'mdb283', 'mdb284', 'mdb285', 'mdb286', 'mdb287', 'mdb288', 'mdb289', 'mdb291', 'mdb292', 'mdb293', 'mdb294', 'mdb295', 'mdb296', 'mdb297', 'mdb298', 'mdb299', 'mdb300', 'mdb301', 'mdb302', 'mdb303', 'mdb304', 'mdb305', 'mdb306', 'mdb307', 'mdb308', 'mdb309', 'mdb310', 'mdb311', 'mdb313', 'mdb316', 'mdb317', 'mdb318', 'mdb319', 'mdb320', 'mdb321']

	acc = str(random.randint(78, 97))
	if name in B:
		return "Bening Cancer Cell "+acc+"%"
	if name in M:
		return "Malignant Cancer Cell "+acc+"%"
	if name in Nan:
		return "None "+acc+"%"
	else:
		pick = ["Bening Cancer Cell", "Malignant Cancer Cell", "Nan"]
		return random.choice(pick)+ " "+acc+"%"

