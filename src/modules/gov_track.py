import urllib2
import json

class Bill():
	
	def __init__(self):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill")
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.allBills = billData

	def bill_by_id(self, bill_id):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill/" + str(bill_id))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billInformation = billData
		return self.billInformation


	def bill_by_resolution_type(self, resolution_type):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?q=" + resolution_type)
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByResolutionType = billData
		return self.billsByResolutionType


	def bill_by_bill_type(self, bill_type):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?bill_type=" + bill_type.lower().replace(" ", "_"))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByBillType = billData
		return self.billsByBillType

	def bill_by_committee(self, committee_name):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/committee?limit=306")
		apiRead = apiCall.read()
		committeeData = json.loads(apiRead)
		apiCall.close()
	
		for committees in committeeData["objects"]:
			if committee_name == committees["name"]:
				committee_ID = committees["id"]	
				break

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?committees=" + str(committee_ID))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByCommittee = billData
		return self.billsByCommittee


	def bill_by_congress(self, congress):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?congress=" + str(congress))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByCongress = billData
		return self.billsByCongress

	def bill_by_cosponsor(self, cosponsorName):

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/person?q=" + cosponsorName.replace(" ", "+"))
		apiRead = apiCall.read()
		cosponsorData = json.loads(apiRead)
		apiCall.close()

		cosponsorID = cosponsorData["objects"][0]["id"]
		

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?cosponsors=" + str(cosponsorID))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByCosponsor = billData
		return self.billsByCosponsor


	def bill_by_current_status(self, current_status):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?current_status=" + current_status.lower().replace(" ", "_"))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByCurrentStatus = billData
		return self.billsByCurrentStatus

	def bill_by_current_status_date(self, current_status_date):
		import datetime

		current_status_date = datetime.datetime(int(current_status_date[0]), int(current_status_date[1]), int(current_status_date[2]))
		current_status_date.strftime('%y%m%d')
		current_status_date = str(current_status_date)
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?current_status_date=" + current_status_date)
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByCurrentStatusDate = billData
		return self.billsByCurrentStatusDate


	def bill_by_introduced_date(self, introduced_date):
		import datetime

		introduced_date = datetime.datetime(int(introduced_date[0]), int(introduced_date[1]), int(introduced_date[2]))
		introduced_date.strftime('%y%m%d')
		introduced_date = str(introduced_date)
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?introduced_date=" + introduced_date)
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByIntroducedDate = billData
		return self.billsByIntroducedDate


	def bill_by_number(self, number):

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?number=" + str(number))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByNumber = billData
		return self.billsByNumber
	
	def bill_by_sponsor(self, sponsorName):

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/person?q=" + sponsorName.replace(" ", "+"))
		apiRead = apiCall.read()
		cosponsorData = json.loads(apiRead)
		apiCall.close()

		sponsorID = cosponsorData["objects"][0]["id"]

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?sponsor=" + str(sponsorID))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsBySponsor = billData
		return self.billsBySponsor

	def bill_by_terms(self, termID):

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?terms=" + str(termID))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByTerms = billData
		return self.billsByTerms


class Cosponsorship(Bill):

	def __init__(self):
		Bill.__init__(self)


	def cosponsorship_by_bill(self, billID):

		billCoSponsorData = Bill().bill_by_id(billID)

		billCoSponsors = []

		for cosponsor in billCoSponsorData["cosponsors"]:
			billCoSponsors.append({"cosponsorID": cosponsor["id"]})
			billCoSponsors.append({"name": cosponsor["name"]})
			print "\n\n"

		self.billCoSponsors = billCoSponsors

		return self.billCoSponsors
	
	def cosponsorship_by_join_date(self, join_date):
		import datetime

		join_date = datetime.datetime(int(join_date[0]), int(join_date[1]), int(join_date[2]))
		join_date.strftime('%y%m%d')
		join_date = str(join_date)
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/cosponsorship?joined=" + join_date + '&limit=5')
		apiRead = apiCall.read()
		joinDateData = json.loads(apiRead)
		apiCall.close()

		self.joinDateData = joinDateData

		cosponsorbyJoinDateList = []

		for cosponsor in joinDateData["objects"]:
			cosponsorbyJoinDateList.append({"cosponsorID": cosponsor["person"]})
		
		for person in cosponsorbyJoinDateList:
			apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/person/" + str(person["cosponsorID"]))
			apiRead = apiCall.read()
			personData = json.loads(apiRead)
			apiCall.close()

			if person["cosponsorID"] == personData["id"]:
				person["name"] = personData["name"]


		self.cosponsorbyJoinDateList = cosponsorbyJoinDateList

		return self.cosponsorbyJoinDateList


	def cosponsorship_by_person(self, cosponsorName):
		self.billsByCosponsor = Bill().bill_by_cosponsor(cosponsorName)
		return self.billsByCosponsor

	def cosponsorship_by_role(self, roleID):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/cosponsorship?role=" + str(roleID))
		apiRead = apiCall.read()
		cosponsorRoleData = json.loads(apiRead)
		apiCall.close()

		self.cosponsorshipRoleData = cosponsorRoleData

		billList = []

		for bill in cosponsorRoleData["objects"]:
			billList.append({"bill": bill["bill"]}) 

		for item in billList:
			data = Bill().bill_by_id(item["bill"])
			item["name"] = data["title"]

		self.billList = billList

		return self.billList


	def cosponsorship_by_cosponsorshipID(self, cosponsorshipID):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/cosponsorship/" + str(cosponsorshipID))
		apiRead = apiCall.read()
		cosponsorRoleData = json.loads(apiRead)
		apiCall.close()

		cosponsorInformation = {}

		cosponsorInformation["cosponsorID"] = cosponsorRoleData["person"]	
		cosponsorInformation["billID"] = cosponsorRoleData["bill"]

		data = Bill().bill_by_id(cosponsorInformation["billID"])

		cosponsorInformation["billName"] = data["title"]

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/person/" + str(cosponsorInformation["cosponsorID"]))
		apiRead = apiCall.read()
		personData = json.loads(apiRead)
		apiCall.close()

		cosponsorInformation["cosponsorName"] = personData["name"]

		self.cosponsorInformation = cosponsorInformation

		return self.cosponsorInformation

class Person():
	def __init__(self):
		pass
		

	def congressperson_by_name(self, firstname, lastname):
		api_call = urllib2.urlopen('https://www.govtrack.us/api/v2/person?q=' + firstname+ '+' + lastname)
		json_string= api_call.read()
		congress_object = json.loads(json_string)
		api_call.close()

		return congress_object

	def congressperson_by_gender(self,gender):
		api_call = urllib2.urlopen('https://www.govtrack.us/api/v2/person?gender=' + gender)
		json_string= api_call.read()
		congress_object = json.loads(json_string)
		api_call.close()

		return congress_object['objects']



	def congressperson_by_id(self,personId):
		api_call = urllib2.urlopen('https://www.govtrack.us/api/v2/person/' + personId)
		json_string= api_call.read()
		congress_object = json.loads(json_string)
		api_call.close()

		return congress_object

	def current_members_of_congress(self):
		api_call = urllib2.urlopen('https://www.govtrack.us/api/v2/role?current=true')
		json_string= api_call.read()
		congress_object = json.loads(json_string)
		api_call.close()

		return congress_object

	def person_role_by_id(self):
		api_call = urllib2.urlopen('https://www.govtrack.us/api/v2/role/')
		json_string= api_call.read()
		congress_object = json.loads(json_string)
		api_call.close()

		return congress_object

	def person_by_party(self):
		api_call = urllib2.urlopen('https://www.govtrack.us/api/v2/role/')
		json_string= api_call.read()
		congress_object = json.loads(json_string)
		api_call.close()

		return congress_object

	def person_by_member_id(self, memberId):
		api_call = urllib2.urlopen('https://www.govtrack.us/api/v2/role?person=' + memberId)
		json_string= api_call.read()
		congress_object = json.loads(json_string)
		api_call.close()

		return congress_object

	def current_member_of_congress_role_type(self):
		api_call = urllib2.urlopen('https://www.govtrack.us/api/v2/role/representative')
		json_string= api_call.read()
		congress_object = json.loads(json_string)
		api_call.close()

		return congress_object

	def person_by_state(self, state):
		api_call = urllib2.urlopen('https://www.govtrack.us/api/v2/role?state=' + state)
		json_string= api_call.read()
		congress_object = json.loads(json_string)
		api_call.close()
		
		return congress_object


class Votes():

	def __init__(self):
		pass
	
	def member_id(self):
		return str(self.parsed_json['objects'][0]['id'])

	def bill_by_id(self,bill_ID):
		#This queries the GovTrack Database for bills and returns the ID of that specific bill
		a = bill_ID
		f = urllib2.urlopen('https://www.govtrack.us/api/v2/bill/' + a)
		json_string = f.read()
		self.parsed_json = json.loads(json_string)
		f.close()
		return self.parsed_json

	def bill_id_by_bill_name(self, billName):
		#This queries the GovTrack Database for bills and returns the ID of that specific bill
		a = billName
		f = GovTrack.urllib2.urlopen('https://www.govtrack.us/api/v2/bill?q=' + self.a.replace(" ","%20")+ '&bill_type=house_bill&current_status=enacted_signed')
		json_string = f.read()
		self.parsed_json = GovTrack.json.loads(json_string)["objects"]
		f.close()

		return self.parsed_json

		#You can filter out whether or non someone was in office of the time of the bill and they weren't in office, you can just not run the program.
	
	def vote_voter_by_id(self, id,bill_ID):
		#id number
		self.ref_id = id
		f = urllib2.urlopen('https://www.govtrack.us/api/v2/vote_voter?person='+ self.ref_id +'&vote='+ bill_ID)
		json_string = f.read()
		self.parsed_json = GovTrack.json.loads(json_string)['objects'][0]['option']
		f.close()

		return self.parsed_json.get('value')

class Committee():

	def __init__(self): 
		f = urllib2.urlopen('https://www.govtrack.us/api/v2/committee?obsolete=false')
		json_string = f.read()
		parsed_json = json.loads(json_string)
		f.close()
		self.committees_list = []
		self.subcommittees_list = []

		#these loops parse through committees and categorize them as main or subcommittees. 
		for committeeName in parsed_json["objects"]:
			try:
				self.committees_list.append([{"name": committeeName['committee']['name']}, {"id": committeeName['committee']['id']}])
				self.subcommittees_list.append([{"name": committeeName['name']}, {"id": committeeName['id']}])
			except:
				self.committees_list.append([{"name": committeeName['name']}, {"id": committeeName['id']}])

		self.combinedLists = self.committees_list + self.subcommittees_list

		#this is the function that gets an ID for the specified committee 
		def getID(self, committeeName):
			for x in self.combinedLists:
				if x[0]["name"] == committeeName:
					self.committee_id = x[1]["id"]
					return str(self.committee_id)

	def details_by_committee_name(self, committeeName): 
 		
			#this api gets the details on each committee, the variable "committeeN" is empty because it needs an input.
		committeeN = committeeName
		committeeVar = Committee().getID(committeeN)
		f = Committee.urllib2.urlopen('https://www.govtrack.us/api/v2/committee_member?committee=' + committeeVar + "&limit=4000")
		json_string = f.read()
		parsed_json = Committee.json.loads(json_string)
		f.close()
		return parsed_json['objects']	

	def members_by_committee_name(self, committeeName):
		CommitteeMemberList = []
		for member in Committee().details_by_committee_name(committeeName):
			CommitteeMemberList.append({'name': member['person']['name'], 'committee_role':member['role_label']})

		return CommitteeMemberList

	def committee_by_id(self,committee_id):
		f = Committee.urllib2.urlopen('https://www.govtrack.us/api/v2/committee/' + committee_id)
		json_string = f.read()
		parsed_json = Committee.json.loads(json_string)
		f.close()

		return parsed_json

	def members_by_committee_id(self, committee_id):
		CommitteeMemberList = []
		for member in Committee().details_by_committee_id(committee_id):
			CommitteeMemberList.append({'name': member['person']['name'], 'committee_role':member['role_label']})

		return CommitteeMemberList

	def details_by_committee_id(self, committee_id): 
		f = Committee.urllib2.urlopen('https://www.govtrack.us/api/v2/committee_member?committee=' + committee_id + "&limit=4000")
		json_string = f.read()
		parsed_json = Committee.json.loads(json_string)
		f.close()

		return parsed_json['objects']





