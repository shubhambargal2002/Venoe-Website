from typing import Union, Any
from atri_react.Flex import Flex
from atri_react.TextBox import TextBox
from manifests.ShadowFlex import ShadowFlex
from manifests.NavFlex import NavFlex
from atri_react.Image import Image
from atri_react.Anchor import Anchor
from atri_react.Dropdown import Dropdown
from manifests.FramerFlex import FramerFlex
from atri_react.Input import Input


  
class Page:
	def __init__(self, state: Union[Any, None]):
		self.event_data = None
		self.event_alias = None
		self._setter_access_tracker = {}
		self.Flex1 = state["Flex1"] if "Flex1" in state else None
		self.TextBox1 = state["TextBox1"] if "TextBox1" in state else None
		self.ShadowFlex1 = state["ShadowFlex1"] if "ShadowFlex1" in state else None
		self.Flex2 = state["Flex2"] if "Flex2" in state else None
		self.NavFlex1 = state["NavFlex1"] if "NavFlex1" in state else None
		self.TextBox2 = state["TextBox2"] if "TextBox2" in state else None
		self.TextBox3 = state["TextBox3"] if "TextBox3" in state else None
		self.NavFlex2 = state["NavFlex2"] if "NavFlex2" in state else None
		self.TextBox4 = state["TextBox4"] if "TextBox4" in state else None
		self.NavFlex3 = state["NavFlex3"] if "NavFlex3" in state else None
		self.TextBox5 = state["TextBox5"] if "TextBox5" in state else None
		self.NavFlex4 = state["NavFlex4"] if "NavFlex4" in state else None
		self.Flex4 = state["Flex4"] if "Flex4" in state else None
		self.Flex5 = state["Flex5"] if "Flex5" in state else None
		self.Flex6 = state["Flex6"] if "Flex6" in state else None
		self.Flex7 = state["Flex7"] if "Flex7" in state else None
		self.Flex8 = state["Flex8"] if "Flex8" in state else None
		self.Image1 = state["Image1"] if "Image1" in state else None
		self.Flex9 = state["Flex9"] if "Flex9" in state else None
		self.Flex10 = state["Flex10"] if "Flex10" in state else None
		self.Anchor1 = state["Anchor1"] if "Anchor1" in state else None
		self.Anchor2 = state["Anchor2"] if "Anchor2" in state else None
		self.Anchor3 = state["Anchor3"] if "Anchor3" in state else None
		self.Anchor4 = state["Anchor4"] if "Anchor4" in state else None
		self.ShadowFlex2 = state["ShadowFlex2"] if "ShadowFlex2" in state else None
		self.TextBox13 = state["TextBox13"] if "TextBox13" in state else None
		self.Anchor5 = state["Anchor5"] if "Anchor5" in state else None
		self.TextBox14 = state["TextBox14"] if "TextBox14" in state else None
		self.ShadowFlex3 = state["ShadowFlex3"] if "ShadowFlex3" in state else None
		self.Anchor6 = state["Anchor6"] if "Anchor6" in state else None
		self.Anchor7 = state["Anchor7"] if "Anchor7" in state else None
		self.Dropdown1 = state["Dropdown1"] if "Dropdown1" in state else None
		self.Flex11 = state["Flex11"] if "Flex11" in state else None
		self.Image2 = state["Image2"] if "Image2" in state else None
		self.Flex12 = state["Flex12"] if "Flex12" in state else None
		self.Flex13 = state["Flex13"] if "Flex13" in state else None
		self.Flex14 = state["Flex14"] if "Flex14" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
		self.TextBox16 = state["TextBox16"] if "TextBox16" in state else None
		self.FramerFlex7 = state["FramerFlex7"] if "FramerFlex7" in state else None
		self.TextBox17 = state["TextBox17"] if "TextBox17" in state else None
		self.FramerFlex8 = state["FramerFlex8"] if "FramerFlex8" in state else None
		self.Anchor8 = state["Anchor8"] if "Anchor8" in state else None
		self.FramerFlex9 = state["FramerFlex9"] if "FramerFlex9" in state else None
		self.FramerFlex10 = state["FramerFlex10"] if "FramerFlex10" in state else None
		self.TextBox18 = state["TextBox18"] if "TextBox18" in state else None
		self.ShadowFlex4 = state["ShadowFlex4"] if "ShadowFlex4" in state else None
		self.Anchor9 = state["Anchor9"] if "Anchor9" in state else None
		self.TextBox19 = state["TextBox19"] if "TextBox19" in state else None
		self.TextBox20 = state["TextBox20"] if "TextBox20" in state else None
		self.FramerFlex11 = state["FramerFlex11"] if "FramerFlex11" in state else None
		self.FramerFlex12 = state["FramerFlex12"] if "FramerFlex12" in state else None
		self.FramerFlex13 = state["FramerFlex13"] if "FramerFlex13" in state else None
		self.Flex15 = state["Flex15"] if "Flex15" in state else None
		self.Flex16 = state["Flex16"] if "Flex16" in state else None
		self.Flex17 = state["Flex17"] if "Flex17" in state else None
		self.Flex18 = state["Flex18"] if "Flex18" in state else None
		self.Flex19 = state["Flex19"] if "Flex19" in state else None
		self.FramerFlex14 = state["FramerFlex14"] if "FramerFlex14" in state else None
		self.TextBox21 = state["TextBox21"] if "TextBox21" in state else None
		self.TextBox22 = state["TextBox22"] if "TextBox22" in state else None
		self.FramerFlex15 = state["FramerFlex15"] if "FramerFlex15" in state else None
		self.Flex20 = state["Flex20"] if "Flex20" in state else None
		self.Flex21 = state["Flex21"] if "Flex21" in state else None
		self.Flex22 = state["Flex22"] if "Flex22" in state else None
		self.Flex23 = state["Flex23"] if "Flex23" in state else None
		self.Flex24 = state["Flex24"] if "Flex24" in state else None
		self.Flex25 = state["Flex25"] if "Flex25" in state else None
		self.FramerFlex16 = state["FramerFlex16"] if "FramerFlex16" in state else None
		self.ShadowFlex5 = state["ShadowFlex5"] if "ShadowFlex5" in state else None
		self.TextBox23 = state["TextBox23"] if "TextBox23" in state else None
		self.TextBox24 = state["TextBox24"] if "TextBox24" in state else None
		self.TextBox25 = state["TextBox25"] if "TextBox25" in state else None
		self.TextBox26 = state["TextBox26"] if "TextBox26" in state else None
		self.ShadowFlex6 = state["ShadowFlex6"] if "ShadowFlex6" in state else None
		self.FramerFlex17 = state["FramerFlex17"] if "FramerFlex17" in state else None
		self.TextBox27 = state["TextBox27"] if "TextBox27" in state else None
		self.TextBox28 = state["TextBox28"] if "TextBox28" in state else None
		self.ShadowFlex7 = state["ShadowFlex7"] if "ShadowFlex7" in state else None
		self.FramerFlex18 = state["FramerFlex18"] if "FramerFlex18" in state else None
		self.TextBox29 = state["TextBox29"] if "TextBox29" in state else None
		self.TextBox30 = state["TextBox30"] if "TextBox30" in state else None
		self.ShadowFlex8 = state["ShadowFlex8"] if "ShadowFlex8" in state else None
		self.FramerFlex19 = state["FramerFlex19"] if "FramerFlex19" in state else None
		self.TextBox31 = state["TextBox31"] if "TextBox31" in state else None
		self.TextBox32 = state["TextBox32"] if "TextBox32" in state else None
		self.ShadowFlex9 = state["ShadowFlex9"] if "ShadowFlex9" in state else None
		self.FramerFlex20 = state["FramerFlex20"] if "FramerFlex20" in state else None
		self.TextBox33 = state["TextBox33"] if "TextBox33" in state else None
		self.TextBox34 = state["TextBox34"] if "TextBox34" in state else None
		self.ShadowFlex10 = state["ShadowFlex10"] if "ShadowFlex10" in state else None
		self.FramerFlex21 = state["FramerFlex21"] if "FramerFlex21" in state else None
		self.TextBox35 = state["TextBox35"] if "TextBox35" in state else None
		self.TextBox36 = state["TextBox36"] if "TextBox36" in state else None
		self.ShadowFlex11 = state["ShadowFlex11"] if "ShadowFlex11" in state else None
		self.FramerFlex22 = state["FramerFlex22"] if "FramerFlex22" in state else None
		self.TextBox37 = state["TextBox37"] if "TextBox37" in state else None
		self.TextBox38 = state["TextBox38"] if "TextBox38" in state else None
		self.ShadowFlex12 = state["ShadowFlex12"] if "ShadowFlex12" in state else None
		self.FramerFlex23 = state["FramerFlex23"] if "FramerFlex23" in state else None
		self.FramerFlex24 = state["FramerFlex24"] if "FramerFlex24" in state else None
		self.TextBox39 = state["TextBox39"] if "TextBox39" in state else None
		self.ShadowFlex13 = state["ShadowFlex13"] if "ShadowFlex13" in state else None
		self.Flex27 = state["Flex27"] if "Flex27" in state else None
		self.Flex28 = state["Flex28"] if "Flex28" in state else None
		self.TextBox40 = state["TextBox40"] if "TextBox40" in state else None
		self.FramerFlex25 = state["FramerFlex25"] if "FramerFlex25" in state else None
		self.TextBox41 = state["TextBox41"] if "TextBox41" in state else None
		self.FramerFlex26 = state["FramerFlex26"] if "FramerFlex26" in state else None
		self.Flex29 = state["Flex29"] if "Flex29" in state else None
		self.Flex30 = state["Flex30"] if "Flex30" in state else None
		self.TextBox42 = state["TextBox42"] if "TextBox42" in state else None
		self.FramerFlex27 = state["FramerFlex27"] if "FramerFlex27" in state else None
		self.TextBox43 = state["TextBox43"] if "TextBox43" in state else None
		self.ShadowFlex14 = state["ShadowFlex14"] if "ShadowFlex14" in state else None
		self.FramerFlex28 = state["FramerFlex28"] if "FramerFlex28" in state else None
		self.Flex31 = state["Flex31"] if "Flex31" in state else None
		self.FramerFlex29 = state["FramerFlex29"] if "FramerFlex29" in state else None
		self.Image4 = state["Image4"] if "Image4" in state else None
		self.Image5 = state["Image5"] if "Image5" in state else None
		self.FramerFlex30 = state["FramerFlex30"] if "FramerFlex30" in state else None
		self.Image6 = state["Image6"] if "Image6" in state else None
		self.FramerFlex31 = state["FramerFlex31"] if "FramerFlex31" in state else None
		self.Image7 = state["Image7"] if "Image7" in state else None
		self.FramerFlex32 = state["FramerFlex32"] if "FramerFlex32" in state else None
		self.Image8 = state["Image8"] if "Image8" in state else None
		self.FramerFlex33 = state["FramerFlex33"] if "FramerFlex33" in state else None
		self.Image9 = state["Image9"] if "Image9" in state else None
		self.FramerFlex34 = state["FramerFlex34"] if "FramerFlex34" in state else None
		self.Flex32 = state["Flex32"] if "Flex32" in state else None
		self.Flex33 = state["Flex33"] if "Flex33" in state else None
		self.TextBox44 = state["TextBox44"] if "TextBox44" in state else None
		self.TextBox45 = state["TextBox45"] if "TextBox45" in state else None
		self.FramerFlex35 = state["FramerFlex35"] if "FramerFlex35" in state else None
		self.FramerFlex36 = state["FramerFlex36"] if "FramerFlex36" in state else None
		self.Flex34 = state["Flex34"] if "Flex34" in state else None
		self.Flex35 = state["Flex35"] if "Flex35" in state else None
		self.FramerFlex37 = state["FramerFlex37"] if "FramerFlex37" in state else None
		self.ShadowFlex15 = state["ShadowFlex15"] if "ShadowFlex15" in state else None
		self.Image10 = state["Image10"] if "Image10" in state else None
		self.Flex36 = state["Flex36"] if "Flex36" in state else None
		self.Flex37 = state["Flex37"] if "Flex37" in state else None
		self.Flex38 = state["Flex38"] if "Flex38" in state else None
		self.TextBox46 = state["TextBox46"] if "TextBox46" in state else None
		self.TextBox47 = state["TextBox47"] if "TextBox47" in state else None
		self.Image11 = state["Image11"] if "Image11" in state else None
		self.Flex39 = state["Flex39"] if "Flex39" in state else None
		self.TextBox48 = state["TextBox48"] if "TextBox48" in state else None
		self.TextBox49 = state["TextBox49"] if "TextBox49" in state else None
		self.TextBox50 = state["TextBox50"] if "TextBox50" in state else None
		self.TextBox51 = state["TextBox51"] if "TextBox51" in state else None
		self.TextBox52 = state["TextBox52"] if "TextBox52" in state else None
		self.TextBox53 = state["TextBox53"] if "TextBox53" in state else None
		self.Flex40 = state["Flex40"] if "Flex40" in state else None
		self.Image12 = state["Image12"] if "Image12" in state else None
		self.Flex41 = state["Flex41"] if "Flex41" in state else None
		self.Flex42 = state["Flex42"] if "Flex42" in state else None
		self.Flex43 = state["Flex43"] if "Flex43" in state else None
		self.Image13 = state["Image13"] if "Image13" in state else None
		self.ShadowFlex16 = state["ShadowFlex16"] if "ShadowFlex16" in state else None
		self.FramerFlex38 = state["FramerFlex38"] if "FramerFlex38" in state else None
		self.TextBox54 = state["TextBox54"] if "TextBox54" in state else None
		self.TextBox55 = state["TextBox55"] if "TextBox55" in state else None
		self.TextBox56 = state["TextBox56"] if "TextBox56" in state else None
		self.TextBox57 = state["TextBox57"] if "TextBox57" in state else None
		self.Flex44 = state["Flex44"] if "Flex44" in state else None
		self.Image14 = state["Image14"] if "Image14" in state else None
		self.Flex45 = state["Flex45"] if "Flex45" in state else None
		self.Flex46 = state["Flex46"] if "Flex46" in state else None
		self.Flex47 = state["Flex47"] if "Flex47" in state else None
		self.Image15 = state["Image15"] if "Image15" in state else None
		self.ShadowFlex17 = state["ShadowFlex17"] if "ShadowFlex17" in state else None
		self.FramerFlex39 = state["FramerFlex39"] if "FramerFlex39" in state else None
		self.Anchor10 = state["Anchor10"] if "Anchor10" in state else None
		self.Anchor11 = state["Anchor11"] if "Anchor11" in state else None
		self.Anchor12 = state["Anchor12"] if "Anchor12" in state else None
		self.TextBox58 = state["TextBox58"] if "TextBox58" in state else None
		self.ShadowFlex18 = state["ShadowFlex18"] if "ShadowFlex18" in state else None
		self.FramerFlex40 = state["FramerFlex40"] if "FramerFlex40" in state else None
		self.Flex48 = state["Flex48"] if "Flex48" in state else None
		self.Anchor13 = state["Anchor13"] if "Anchor13" in state else None
		self.Anchor14 = state["Anchor14"] if "Anchor14" in state else None
		self.Anchor15 = state["Anchor15"] if "Anchor15" in state else None
		self.Flex49 = state["Flex49"] if "Flex49" in state else None
		self.Flex50 = state["Flex50"] if "Flex50" in state else None
		self.Flex51 = state["Flex51"] if "Flex51" in state else None
		self.Flex52 = state["Flex52"] if "Flex52" in state else None
		self.Flex53 = state["Flex53"] if "Flex53" in state else None
		self.Flex54 = state["Flex54"] if "Flex54" in state else None
		self.Image16 = state["Image16"] if "Image16" in state else None
		self.TextBox59 = state["TextBox59"] if "TextBox59" in state else None
		self.Flex55 = state["Flex55"] if "Flex55" in state else None
		self.Flex56 = state["Flex56"] if "Flex56" in state else None
		self.TextBox60 = state["TextBox60"] if "TextBox60" in state else None
		self.Input1 = state["Input1"] if "Input1" in state else None
		self.TextBox61 = state["TextBox61"] if "TextBox61" in state else None
		self.ShadowFlex19 = state["ShadowFlex19"] if "ShadowFlex19" in state else None
		self.Flex57 = state["Flex57"] if "Flex57" in state else None
		self.Flex58 = state["Flex58"] if "Flex58" in state else None
		self.TextBox62 = state["TextBox62"] if "TextBox62" in state else None
		self.TextBox63 = state["TextBox63"] if "TextBox63" in state else None
		self.Flex59 = state["Flex59"] if "Flex59" in state else None
		self.Flex60 = state["Flex60"] if "Flex60" in state else None
		self.TextBox64 = state["TextBox64"] if "TextBox64" in state else None
		self.TextBox65 = state["TextBox65"] if "TextBox65" in state else None
		self.TextBox66 = state["TextBox66"] if "TextBox66" in state else None
		self.TextBox67 = state["TextBox67"] if "TextBox67" in state else None
		self.TextBox68 = state["TextBox68"] if "TextBox68" in state else None
		self.TextBox69 = state["TextBox69"] if "TextBox69" in state else None
		self.TextBox70 = state["TextBox70"] if "TextBox70" in state else None
		self.Anchor16 = state["Anchor16"] if "Anchor16" in state else None
		self.Anchor17 = state["Anchor17"] if "Anchor17" in state else None
		self.Anchor18 = state["Anchor18"] if "Anchor18" in state else None
		self.Anchor19 = state["Anchor19"] if "Anchor19" in state else None
		self.Anchor20 = state["Anchor20"] if "Anchor20" in state else None
		self.Anchor21 = state["Anchor21"] if "Anchor21" in state else None
		self.Anchor22 = state["Anchor22"] if "Anchor22" in state else None
		self.NavFlex5 = state["NavFlex5"] if "NavFlex5" in state else None
		self.NavFlex6 = state["NavFlex6"] if "NavFlex6" in state else None
		self.NavFlex7 = state["NavFlex7"] if "NavFlex7" in state else None
		self.NavFlex8 = state["NavFlex8"] if "NavFlex8" in state else None
		self.NavFlex9 = state["NavFlex9"] if "NavFlex9" in state else None
		self.NavFlex10 = state["NavFlex10"] if "NavFlex10" in state else None
		self.NavFlex11 = state["NavFlex11"] if "NavFlex11" in state else None
		self.NavFlex12 = state["NavFlex12"] if "NavFlex12" in state else None
		self.Anchor23 = state["Anchor23"] if "Anchor23" in state else None
		self.Image17 = state["Image17"] if "Image17" in state else None
		self.TextBox71 = state["TextBox71"] if "TextBox71" in state else None
		self.TextBox72 = state["TextBox72"] if "TextBox72" in state else None
		self.Image18 = state["Image18"] if "Image18" in state else None
		self.NavFlex13 = state["NavFlex13"] if "NavFlex13" in state else None
		self.Anchor24 = state["Anchor24"] if "Anchor24" in state else None
		self.TextBox73 = state["TextBox73"] if "TextBox73" in state else None
		self.Image19 = state["Image19"] if "Image19" in state else None
		self.NavFlex14 = state["NavFlex14"] if "NavFlex14" in state else None
		self.Anchor25 = state["Anchor25"] if "Anchor25" in state else None
		self.TextBox74 = state["TextBox74"] if "TextBox74" in state else None
		self.Image20 = state["Image20"] if "Image20" in state else None
		self.NavFlex15 = state["NavFlex15"] if "NavFlex15" in state else None
		self.Anchor26 = state["Anchor26"] if "Anchor26" in state else None
		self.TextBox75 = state["TextBox75"] if "TextBox75" in state else None
		self.Flex61 = state["Flex61"] if "Flex61" in state else None
		self.Anchor27 = state["Anchor27"] if "Anchor27" in state else None
		self.NavFlex16 = state["NavFlex16"] if "NavFlex16" in state else None
		self.TextBox77 = state["TextBox77"] if "TextBox77" in state else None
		self.TextBox78 = state["TextBox78"] if "TextBox78" in state else None
		self.NavFlex17 = state["NavFlex17"] if "NavFlex17" in state else None
		self.Anchor28 = state["Anchor28"] if "Anchor28" in state else None
		self.TextBox79 = state["TextBox79"] if "TextBox79" in state else None
		self.NavFlex18 = state["NavFlex18"] if "NavFlex18" in state else None
		self.Anchor29 = state["Anchor29"] if "Anchor29" in state else None
		self.TextBox80 = state["TextBox80"] if "TextBox80" in state else None
		self.TextBox81 = state["TextBox81"] if "TextBox81" in state else None
		self.TextBox82 = state["TextBox82"] if "TextBox82" in state else None
		self.NavFlex19 = state["NavFlex19"] if "NavFlex19" in state else None
		self.NavFlex20 = state["NavFlex20"] if "NavFlex20" in state else None
		self.NavFlex21 = state["NavFlex21"] if "NavFlex21" in state else None
		self.Anchor30 = state["Anchor30"] if "Anchor30" in state else None
		self.Anchor31 = state["Anchor31"] if "Anchor31" in state else None
		self.Anchor32 = state["Anchor32"] if "Anchor32" in state else None
		self.Flex62 = state["Flex62"] if "Flex62" in state else None
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}
  
	def set_event(self, event):
		self.event_data = event["event_data"]
		self.event_alias = event["alias"]
		callback_name = event["callback_name"]
		if hasattr(self, self.event_alias):
			comp = getattr(self, self.event_alias)
			setattr(comp, callback_name, True)
		self.event_repeating = event["repeating"]
  
	
	@property
	def Flex1(self):
		self._getter_access_tracker["Flex1"] = {}
		return self._Flex1
	@Flex1.setter
	def Flex1(self, new_state):
		self._setter_access_tracker["Flex1"] = {}
		self._Flex1 = Flex(new_state)

	@property
	def TextBox1(self):
		self._getter_access_tracker["TextBox1"] = {}
		return self._TextBox1
	@TextBox1.setter
	def TextBox1(self, new_state):
		self._setter_access_tracker["TextBox1"] = {}
		self._TextBox1 = TextBox(new_state)

	@property
	def ShadowFlex1(self):
		self._getter_access_tracker["ShadowFlex1"] = {}
		return self._ShadowFlex1
	@ShadowFlex1.setter
	def ShadowFlex1(self, new_state):
		self._setter_access_tracker["ShadowFlex1"] = {}
		self._ShadowFlex1 = ShadowFlex(new_state)

	@property
	def Flex2(self):
		self._getter_access_tracker["Flex2"] = {}
		return self._Flex2
	@Flex2.setter
	def Flex2(self, new_state):
		self._setter_access_tracker["Flex2"] = {}
		self._Flex2 = Flex(new_state)

	@property
	def NavFlex1(self):
		self._getter_access_tracker["NavFlex1"] = {}
		return self._NavFlex1
	@NavFlex1.setter
	def NavFlex1(self, new_state):
		self._setter_access_tracker["NavFlex1"] = {}
		self._NavFlex1 = NavFlex(new_state)

	@property
	def TextBox2(self):
		self._getter_access_tracker["TextBox2"] = {}
		return self._TextBox2
	@TextBox2.setter
	def TextBox2(self, new_state):
		self._setter_access_tracker["TextBox2"] = {}
		self._TextBox2 = TextBox(new_state)

	@property
	def TextBox3(self):
		self._getter_access_tracker["TextBox3"] = {}
		return self._TextBox3
	@TextBox3.setter
	def TextBox3(self, new_state):
		self._setter_access_tracker["TextBox3"] = {}
		self._TextBox3 = TextBox(new_state)

	@property
	def NavFlex2(self):
		self._getter_access_tracker["NavFlex2"] = {}
		return self._NavFlex2
	@NavFlex2.setter
	def NavFlex2(self, new_state):
		self._setter_access_tracker["NavFlex2"] = {}
		self._NavFlex2 = NavFlex(new_state)

	@property
	def TextBox4(self):
		self._getter_access_tracker["TextBox4"] = {}
		return self._TextBox4
	@TextBox4.setter
	def TextBox4(self, new_state):
		self._setter_access_tracker["TextBox4"] = {}
		self._TextBox4 = TextBox(new_state)

	@property
	def NavFlex3(self):
		self._getter_access_tracker["NavFlex3"] = {}
		return self._NavFlex3
	@NavFlex3.setter
	def NavFlex3(self, new_state):
		self._setter_access_tracker["NavFlex3"] = {}
		self._NavFlex3 = NavFlex(new_state)

	@property
	def TextBox5(self):
		self._getter_access_tracker["TextBox5"] = {}
		return self._TextBox5
	@TextBox5.setter
	def TextBox5(self, new_state):
		self._setter_access_tracker["TextBox5"] = {}
		self._TextBox5 = TextBox(new_state)

	@property
	def NavFlex4(self):
		self._getter_access_tracker["NavFlex4"] = {}
		return self._NavFlex4
	@NavFlex4.setter
	def NavFlex4(self, new_state):
		self._setter_access_tracker["NavFlex4"] = {}
		self._NavFlex4 = NavFlex(new_state)

	@property
	def Flex4(self):
		self._getter_access_tracker["Flex4"] = {}
		return self._Flex4
	@Flex4.setter
	def Flex4(self, new_state):
		self._setter_access_tracker["Flex4"] = {}
		self._Flex4 = Flex(new_state)

	@property
	def Flex5(self):
		self._getter_access_tracker["Flex5"] = {}
		return self._Flex5
	@Flex5.setter
	def Flex5(self, new_state):
		self._setter_access_tracker["Flex5"] = {}
		self._Flex5 = Flex(new_state)

	@property
	def Flex6(self):
		self._getter_access_tracker["Flex6"] = {}
		return self._Flex6
	@Flex6.setter
	def Flex6(self, new_state):
		self._setter_access_tracker["Flex6"] = {}
		self._Flex6 = Flex(new_state)

	@property
	def Flex7(self):
		self._getter_access_tracker["Flex7"] = {}
		return self._Flex7
	@Flex7.setter
	def Flex7(self, new_state):
		self._setter_access_tracker["Flex7"] = {}
		self._Flex7 = Flex(new_state)

	@property
	def Flex8(self):
		self._getter_access_tracker["Flex8"] = {}
		return self._Flex8
	@Flex8.setter
	def Flex8(self, new_state):
		self._setter_access_tracker["Flex8"] = {}
		self._Flex8 = Flex(new_state)

	@property
	def Image1(self):
		self._getter_access_tracker["Image1"] = {}
		return self._Image1
	@Image1.setter
	def Image1(self, new_state):
		self._setter_access_tracker["Image1"] = {}
		self._Image1 = Image(new_state)

	@property
	def Flex9(self):
		self._getter_access_tracker["Flex9"] = {}
		return self._Flex9
	@Flex9.setter
	def Flex9(self, new_state):
		self._setter_access_tracker["Flex9"] = {}
		self._Flex9 = Flex(new_state)

	@property
	def Flex10(self):
		self._getter_access_tracker["Flex10"] = {}
		return self._Flex10
	@Flex10.setter
	def Flex10(self, new_state):
		self._setter_access_tracker["Flex10"] = {}
		self._Flex10 = Flex(new_state)

	@property
	def Anchor1(self):
		self._getter_access_tracker["Anchor1"] = {}
		return self._Anchor1
	@Anchor1.setter
	def Anchor1(self, new_state):
		self._setter_access_tracker["Anchor1"] = {}
		self._Anchor1 = Anchor(new_state)

	@property
	def Anchor2(self):
		self._getter_access_tracker["Anchor2"] = {}
		return self._Anchor2
	@Anchor2.setter
	def Anchor2(self, new_state):
		self._setter_access_tracker["Anchor2"] = {}
		self._Anchor2 = Anchor(new_state)

	@property
	def Anchor3(self):
		self._getter_access_tracker["Anchor3"] = {}
		return self._Anchor3
	@Anchor3.setter
	def Anchor3(self, new_state):
		self._setter_access_tracker["Anchor3"] = {}
		self._Anchor3 = Anchor(new_state)

	@property
	def Anchor4(self):
		self._getter_access_tracker["Anchor4"] = {}
		return self._Anchor4
	@Anchor4.setter
	def Anchor4(self, new_state):
		self._setter_access_tracker["Anchor4"] = {}
		self._Anchor4 = Anchor(new_state)

	@property
	def ShadowFlex2(self):
		self._getter_access_tracker["ShadowFlex2"] = {}
		return self._ShadowFlex2
	@ShadowFlex2.setter
	def ShadowFlex2(self, new_state):
		self._setter_access_tracker["ShadowFlex2"] = {}
		self._ShadowFlex2 = ShadowFlex(new_state)

	@property
	def TextBox13(self):
		self._getter_access_tracker["TextBox13"] = {}
		return self._TextBox13
	@TextBox13.setter
	def TextBox13(self, new_state):
		self._setter_access_tracker["TextBox13"] = {}
		self._TextBox13 = TextBox(new_state)

	@property
	def Anchor5(self):
		self._getter_access_tracker["Anchor5"] = {}
		return self._Anchor5
	@Anchor5.setter
	def Anchor5(self, new_state):
		self._setter_access_tracker["Anchor5"] = {}
		self._Anchor5 = Anchor(new_state)

	@property
	def TextBox14(self):
		self._getter_access_tracker["TextBox14"] = {}
		return self._TextBox14
	@TextBox14.setter
	def TextBox14(self, new_state):
		self._setter_access_tracker["TextBox14"] = {}
		self._TextBox14 = TextBox(new_state)

	@property
	def ShadowFlex3(self):
		self._getter_access_tracker["ShadowFlex3"] = {}
		return self._ShadowFlex3
	@ShadowFlex3.setter
	def ShadowFlex3(self, new_state):
		self._setter_access_tracker["ShadowFlex3"] = {}
		self._ShadowFlex3 = ShadowFlex(new_state)

	@property
	def Anchor6(self):
		self._getter_access_tracker["Anchor6"] = {}
		return self._Anchor6
	@Anchor6.setter
	def Anchor6(self, new_state):
		self._setter_access_tracker["Anchor6"] = {}
		self._Anchor6 = Anchor(new_state)

	@property
	def Anchor7(self):
		self._getter_access_tracker["Anchor7"] = {}
		return self._Anchor7
	@Anchor7.setter
	def Anchor7(self, new_state):
		self._setter_access_tracker["Anchor7"] = {}
		self._Anchor7 = Anchor(new_state)

	@property
	def Dropdown1(self):
		self._getter_access_tracker["Dropdown1"] = {}
		return self._Dropdown1
	@Dropdown1.setter
	def Dropdown1(self, new_state):
		self._setter_access_tracker["Dropdown1"] = {}
		self._Dropdown1 = Dropdown(new_state)

	@property
	def Flex11(self):
		self._getter_access_tracker["Flex11"] = {}
		return self._Flex11
	@Flex11.setter
	def Flex11(self, new_state):
		self._setter_access_tracker["Flex11"] = {}
		self._Flex11 = Flex(new_state)

	@property
	def Image2(self):
		self._getter_access_tracker["Image2"] = {}
		return self._Image2
	@Image2.setter
	def Image2(self, new_state):
		self._setter_access_tracker["Image2"] = {}
		self._Image2 = Image(new_state)

	@property
	def Flex12(self):
		self._getter_access_tracker["Flex12"] = {}
		return self._Flex12
	@Flex12.setter
	def Flex12(self, new_state):
		self._setter_access_tracker["Flex12"] = {}
		self._Flex12 = Flex(new_state)

	@property
	def Flex13(self):
		self._getter_access_tracker["Flex13"] = {}
		return self._Flex13
	@Flex13.setter
	def Flex13(self, new_state):
		self._setter_access_tracker["Flex13"] = {}
		self._Flex13 = Flex(new_state)

	@property
	def Flex14(self):
		self._getter_access_tracker["Flex14"] = {}
		return self._Flex14
	@Flex14.setter
	def Flex14(self, new_state):
		self._setter_access_tracker["Flex14"] = {}
		self._Flex14 = Flex(new_state)

	@property
	def Image3(self):
		self._getter_access_tracker["Image3"] = {}
		return self._Image3
	@Image3.setter
	def Image3(self, new_state):
		self._setter_access_tracker["Image3"] = {}
		self._Image3 = Image(new_state)

	@property
	def TextBox16(self):
		self._getter_access_tracker["TextBox16"] = {}
		return self._TextBox16
	@TextBox16.setter
	def TextBox16(self, new_state):
		self._setter_access_tracker["TextBox16"] = {}
		self._TextBox16 = TextBox(new_state)

	@property
	def FramerFlex7(self):
		self._getter_access_tracker["FramerFlex7"] = {}
		return self._FramerFlex7
	@FramerFlex7.setter
	def FramerFlex7(self, new_state):
		self._setter_access_tracker["FramerFlex7"] = {}
		self._FramerFlex7 = FramerFlex(new_state)

	@property
	def TextBox17(self):
		self._getter_access_tracker["TextBox17"] = {}
		return self._TextBox17
	@TextBox17.setter
	def TextBox17(self, new_state):
		self._setter_access_tracker["TextBox17"] = {}
		self._TextBox17 = TextBox(new_state)

	@property
	def FramerFlex8(self):
		self._getter_access_tracker["FramerFlex8"] = {}
		return self._FramerFlex8
	@FramerFlex8.setter
	def FramerFlex8(self, new_state):
		self._setter_access_tracker["FramerFlex8"] = {}
		self._FramerFlex8 = FramerFlex(new_state)

	@property
	def Anchor8(self):
		self._getter_access_tracker["Anchor8"] = {}
		return self._Anchor8
	@Anchor8.setter
	def Anchor8(self, new_state):
		self._setter_access_tracker["Anchor8"] = {}
		self._Anchor8 = Anchor(new_state)

	@property
	def FramerFlex9(self):
		self._getter_access_tracker["FramerFlex9"] = {}
		return self._FramerFlex9
	@FramerFlex9.setter
	def FramerFlex9(self, new_state):
		self._setter_access_tracker["FramerFlex9"] = {}
		self._FramerFlex9 = FramerFlex(new_state)

	@property
	def FramerFlex10(self):
		self._getter_access_tracker["FramerFlex10"] = {}
		return self._FramerFlex10
	@FramerFlex10.setter
	def FramerFlex10(self, new_state):
		self._setter_access_tracker["FramerFlex10"] = {}
		self._FramerFlex10 = FramerFlex(new_state)

	@property
	def TextBox18(self):
		self._getter_access_tracker["TextBox18"] = {}
		return self._TextBox18
	@TextBox18.setter
	def TextBox18(self, new_state):
		self._setter_access_tracker["TextBox18"] = {}
		self._TextBox18 = TextBox(new_state)

	@property
	def ShadowFlex4(self):
		self._getter_access_tracker["ShadowFlex4"] = {}
		return self._ShadowFlex4
	@ShadowFlex4.setter
	def ShadowFlex4(self, new_state):
		self._setter_access_tracker["ShadowFlex4"] = {}
		self._ShadowFlex4 = ShadowFlex(new_state)

	@property
	def Anchor9(self):
		self._getter_access_tracker["Anchor9"] = {}
		return self._Anchor9
	@Anchor9.setter
	def Anchor9(self, new_state):
		self._setter_access_tracker["Anchor9"] = {}
		self._Anchor9 = Anchor(new_state)

	@property
	def TextBox19(self):
		self._getter_access_tracker["TextBox19"] = {}
		return self._TextBox19
	@TextBox19.setter
	def TextBox19(self, new_state):
		self._setter_access_tracker["TextBox19"] = {}
		self._TextBox19 = TextBox(new_state)

	@property
	def TextBox20(self):
		self._getter_access_tracker["TextBox20"] = {}
		return self._TextBox20
	@TextBox20.setter
	def TextBox20(self, new_state):
		self._setter_access_tracker["TextBox20"] = {}
		self._TextBox20 = TextBox(new_state)

	@property
	def FramerFlex11(self):
		self._getter_access_tracker["FramerFlex11"] = {}
		return self._FramerFlex11
	@FramerFlex11.setter
	def FramerFlex11(self, new_state):
		self._setter_access_tracker["FramerFlex11"] = {}
		self._FramerFlex11 = FramerFlex(new_state)

	@property
	def FramerFlex12(self):
		self._getter_access_tracker["FramerFlex12"] = {}
		return self._FramerFlex12
	@FramerFlex12.setter
	def FramerFlex12(self, new_state):
		self._setter_access_tracker["FramerFlex12"] = {}
		self._FramerFlex12 = FramerFlex(new_state)

	@property
	def FramerFlex13(self):
		self._getter_access_tracker["FramerFlex13"] = {}
		return self._FramerFlex13
	@FramerFlex13.setter
	def FramerFlex13(self, new_state):
		self._setter_access_tracker["FramerFlex13"] = {}
		self._FramerFlex13 = FramerFlex(new_state)

	@property
	def Flex15(self):
		self._getter_access_tracker["Flex15"] = {}
		return self._Flex15
	@Flex15.setter
	def Flex15(self, new_state):
		self._setter_access_tracker["Flex15"] = {}
		self._Flex15 = Flex(new_state)

	@property
	def Flex16(self):
		self._getter_access_tracker["Flex16"] = {}
		return self._Flex16
	@Flex16.setter
	def Flex16(self, new_state):
		self._setter_access_tracker["Flex16"] = {}
		self._Flex16 = Flex(new_state)

	@property
	def Flex17(self):
		self._getter_access_tracker["Flex17"] = {}
		return self._Flex17
	@Flex17.setter
	def Flex17(self, new_state):
		self._setter_access_tracker["Flex17"] = {}
		self._Flex17 = Flex(new_state)

	@property
	def Flex18(self):
		self._getter_access_tracker["Flex18"] = {}
		return self._Flex18
	@Flex18.setter
	def Flex18(self, new_state):
		self._setter_access_tracker["Flex18"] = {}
		self._Flex18 = Flex(new_state)

	@property
	def Flex19(self):
		self._getter_access_tracker["Flex19"] = {}
		return self._Flex19
	@Flex19.setter
	def Flex19(self, new_state):
		self._setter_access_tracker["Flex19"] = {}
		self._Flex19 = Flex(new_state)

	@property
	def FramerFlex14(self):
		self._getter_access_tracker["FramerFlex14"] = {}
		return self._FramerFlex14
	@FramerFlex14.setter
	def FramerFlex14(self, new_state):
		self._setter_access_tracker["FramerFlex14"] = {}
		self._FramerFlex14 = FramerFlex(new_state)

	@property
	def TextBox21(self):
		self._getter_access_tracker["TextBox21"] = {}
		return self._TextBox21
	@TextBox21.setter
	def TextBox21(self, new_state):
		self._setter_access_tracker["TextBox21"] = {}
		self._TextBox21 = TextBox(new_state)

	@property
	def TextBox22(self):
		self._getter_access_tracker["TextBox22"] = {}
		return self._TextBox22
	@TextBox22.setter
	def TextBox22(self, new_state):
		self._setter_access_tracker["TextBox22"] = {}
		self._TextBox22 = TextBox(new_state)

	@property
	def FramerFlex15(self):
		self._getter_access_tracker["FramerFlex15"] = {}
		return self._FramerFlex15
	@FramerFlex15.setter
	def FramerFlex15(self, new_state):
		self._setter_access_tracker["FramerFlex15"] = {}
		self._FramerFlex15 = FramerFlex(new_state)

	@property
	def Flex20(self):
		self._getter_access_tracker["Flex20"] = {}
		return self._Flex20
	@Flex20.setter
	def Flex20(self, new_state):
		self._setter_access_tracker["Flex20"] = {}
		self._Flex20 = Flex(new_state)

	@property
	def Flex21(self):
		self._getter_access_tracker["Flex21"] = {}
		return self._Flex21
	@Flex21.setter
	def Flex21(self, new_state):
		self._setter_access_tracker["Flex21"] = {}
		self._Flex21 = Flex(new_state)

	@property
	def Flex22(self):
		self._getter_access_tracker["Flex22"] = {}
		return self._Flex22
	@Flex22.setter
	def Flex22(self, new_state):
		self._setter_access_tracker["Flex22"] = {}
		self._Flex22 = Flex(new_state)

	@property
	def Flex23(self):
		self._getter_access_tracker["Flex23"] = {}
		return self._Flex23
	@Flex23.setter
	def Flex23(self, new_state):
		self._setter_access_tracker["Flex23"] = {}
		self._Flex23 = Flex(new_state)

	@property
	def Flex24(self):
		self._getter_access_tracker["Flex24"] = {}
		return self._Flex24
	@Flex24.setter
	def Flex24(self, new_state):
		self._setter_access_tracker["Flex24"] = {}
		self._Flex24 = Flex(new_state)

	@property
	def Flex25(self):
		self._getter_access_tracker["Flex25"] = {}
		return self._Flex25
	@Flex25.setter
	def Flex25(self, new_state):
		self._setter_access_tracker["Flex25"] = {}
		self._Flex25 = Flex(new_state)

	@property
	def FramerFlex16(self):
		self._getter_access_tracker["FramerFlex16"] = {}
		return self._FramerFlex16
	@FramerFlex16.setter
	def FramerFlex16(self, new_state):
		self._setter_access_tracker["FramerFlex16"] = {}
		self._FramerFlex16 = FramerFlex(new_state)

	@property
	def ShadowFlex5(self):
		self._getter_access_tracker["ShadowFlex5"] = {}
		return self._ShadowFlex5
	@ShadowFlex5.setter
	def ShadowFlex5(self, new_state):
		self._setter_access_tracker["ShadowFlex5"] = {}
		self._ShadowFlex5 = ShadowFlex(new_state)

	@property
	def TextBox23(self):
		self._getter_access_tracker["TextBox23"] = {}
		return self._TextBox23
	@TextBox23.setter
	def TextBox23(self, new_state):
		self._setter_access_tracker["TextBox23"] = {}
		self._TextBox23 = TextBox(new_state)

	@property
	def TextBox24(self):
		self._getter_access_tracker["TextBox24"] = {}
		return self._TextBox24
	@TextBox24.setter
	def TextBox24(self, new_state):
		self._setter_access_tracker["TextBox24"] = {}
		self._TextBox24 = TextBox(new_state)

	@property
	def TextBox25(self):
		self._getter_access_tracker["TextBox25"] = {}
		return self._TextBox25
	@TextBox25.setter
	def TextBox25(self, new_state):
		self._setter_access_tracker["TextBox25"] = {}
		self._TextBox25 = TextBox(new_state)

	@property
	def TextBox26(self):
		self._getter_access_tracker["TextBox26"] = {}
		return self._TextBox26
	@TextBox26.setter
	def TextBox26(self, new_state):
		self._setter_access_tracker["TextBox26"] = {}
		self._TextBox26 = TextBox(new_state)

	@property
	def ShadowFlex6(self):
		self._getter_access_tracker["ShadowFlex6"] = {}
		return self._ShadowFlex6
	@ShadowFlex6.setter
	def ShadowFlex6(self, new_state):
		self._setter_access_tracker["ShadowFlex6"] = {}
		self._ShadowFlex6 = ShadowFlex(new_state)

	@property
	def FramerFlex17(self):
		self._getter_access_tracker["FramerFlex17"] = {}
		return self._FramerFlex17
	@FramerFlex17.setter
	def FramerFlex17(self, new_state):
		self._setter_access_tracker["FramerFlex17"] = {}
		self._FramerFlex17 = FramerFlex(new_state)

	@property
	def TextBox27(self):
		self._getter_access_tracker["TextBox27"] = {}
		return self._TextBox27
	@TextBox27.setter
	def TextBox27(self, new_state):
		self._setter_access_tracker["TextBox27"] = {}
		self._TextBox27 = TextBox(new_state)

	@property
	def TextBox28(self):
		self._getter_access_tracker["TextBox28"] = {}
		return self._TextBox28
	@TextBox28.setter
	def TextBox28(self, new_state):
		self._setter_access_tracker["TextBox28"] = {}
		self._TextBox28 = TextBox(new_state)

	@property
	def ShadowFlex7(self):
		self._getter_access_tracker["ShadowFlex7"] = {}
		return self._ShadowFlex7
	@ShadowFlex7.setter
	def ShadowFlex7(self, new_state):
		self._setter_access_tracker["ShadowFlex7"] = {}
		self._ShadowFlex7 = ShadowFlex(new_state)

	@property
	def FramerFlex18(self):
		self._getter_access_tracker["FramerFlex18"] = {}
		return self._FramerFlex18
	@FramerFlex18.setter
	def FramerFlex18(self, new_state):
		self._setter_access_tracker["FramerFlex18"] = {}
		self._FramerFlex18 = FramerFlex(new_state)

	@property
	def TextBox29(self):
		self._getter_access_tracker["TextBox29"] = {}
		return self._TextBox29
	@TextBox29.setter
	def TextBox29(self, new_state):
		self._setter_access_tracker["TextBox29"] = {}
		self._TextBox29 = TextBox(new_state)

	@property
	def TextBox30(self):
		self._getter_access_tracker["TextBox30"] = {}
		return self._TextBox30
	@TextBox30.setter
	def TextBox30(self, new_state):
		self._setter_access_tracker["TextBox30"] = {}
		self._TextBox30 = TextBox(new_state)

	@property
	def ShadowFlex8(self):
		self._getter_access_tracker["ShadowFlex8"] = {}
		return self._ShadowFlex8
	@ShadowFlex8.setter
	def ShadowFlex8(self, new_state):
		self._setter_access_tracker["ShadowFlex8"] = {}
		self._ShadowFlex8 = ShadowFlex(new_state)

	@property
	def FramerFlex19(self):
		self._getter_access_tracker["FramerFlex19"] = {}
		return self._FramerFlex19
	@FramerFlex19.setter
	def FramerFlex19(self, new_state):
		self._setter_access_tracker["FramerFlex19"] = {}
		self._FramerFlex19 = FramerFlex(new_state)

	@property
	def TextBox31(self):
		self._getter_access_tracker["TextBox31"] = {}
		return self._TextBox31
	@TextBox31.setter
	def TextBox31(self, new_state):
		self._setter_access_tracker["TextBox31"] = {}
		self._TextBox31 = TextBox(new_state)

	@property
	def TextBox32(self):
		self._getter_access_tracker["TextBox32"] = {}
		return self._TextBox32
	@TextBox32.setter
	def TextBox32(self, new_state):
		self._setter_access_tracker["TextBox32"] = {}
		self._TextBox32 = TextBox(new_state)

	@property
	def ShadowFlex9(self):
		self._getter_access_tracker["ShadowFlex9"] = {}
		return self._ShadowFlex9
	@ShadowFlex9.setter
	def ShadowFlex9(self, new_state):
		self._setter_access_tracker["ShadowFlex9"] = {}
		self._ShadowFlex9 = ShadowFlex(new_state)

	@property
	def FramerFlex20(self):
		self._getter_access_tracker["FramerFlex20"] = {}
		return self._FramerFlex20
	@FramerFlex20.setter
	def FramerFlex20(self, new_state):
		self._setter_access_tracker["FramerFlex20"] = {}
		self._FramerFlex20 = FramerFlex(new_state)

	@property
	def TextBox33(self):
		self._getter_access_tracker["TextBox33"] = {}
		return self._TextBox33
	@TextBox33.setter
	def TextBox33(self, new_state):
		self._setter_access_tracker["TextBox33"] = {}
		self._TextBox33 = TextBox(new_state)

	@property
	def TextBox34(self):
		self._getter_access_tracker["TextBox34"] = {}
		return self._TextBox34
	@TextBox34.setter
	def TextBox34(self, new_state):
		self._setter_access_tracker["TextBox34"] = {}
		self._TextBox34 = TextBox(new_state)

	@property
	def ShadowFlex10(self):
		self._getter_access_tracker["ShadowFlex10"] = {}
		return self._ShadowFlex10
	@ShadowFlex10.setter
	def ShadowFlex10(self, new_state):
		self._setter_access_tracker["ShadowFlex10"] = {}
		self._ShadowFlex10 = ShadowFlex(new_state)

	@property
	def FramerFlex21(self):
		self._getter_access_tracker["FramerFlex21"] = {}
		return self._FramerFlex21
	@FramerFlex21.setter
	def FramerFlex21(self, new_state):
		self._setter_access_tracker["FramerFlex21"] = {}
		self._FramerFlex21 = FramerFlex(new_state)

	@property
	def TextBox35(self):
		self._getter_access_tracker["TextBox35"] = {}
		return self._TextBox35
	@TextBox35.setter
	def TextBox35(self, new_state):
		self._setter_access_tracker["TextBox35"] = {}
		self._TextBox35 = TextBox(new_state)

	@property
	def TextBox36(self):
		self._getter_access_tracker["TextBox36"] = {}
		return self._TextBox36
	@TextBox36.setter
	def TextBox36(self, new_state):
		self._setter_access_tracker["TextBox36"] = {}
		self._TextBox36 = TextBox(new_state)

	@property
	def ShadowFlex11(self):
		self._getter_access_tracker["ShadowFlex11"] = {}
		return self._ShadowFlex11
	@ShadowFlex11.setter
	def ShadowFlex11(self, new_state):
		self._setter_access_tracker["ShadowFlex11"] = {}
		self._ShadowFlex11 = ShadowFlex(new_state)

	@property
	def FramerFlex22(self):
		self._getter_access_tracker["FramerFlex22"] = {}
		return self._FramerFlex22
	@FramerFlex22.setter
	def FramerFlex22(self, new_state):
		self._setter_access_tracker["FramerFlex22"] = {}
		self._FramerFlex22 = FramerFlex(new_state)

	@property
	def TextBox37(self):
		self._getter_access_tracker["TextBox37"] = {}
		return self._TextBox37
	@TextBox37.setter
	def TextBox37(self, new_state):
		self._setter_access_tracker["TextBox37"] = {}
		self._TextBox37 = TextBox(new_state)

	@property
	def TextBox38(self):
		self._getter_access_tracker["TextBox38"] = {}
		return self._TextBox38
	@TextBox38.setter
	def TextBox38(self, new_state):
		self._setter_access_tracker["TextBox38"] = {}
		self._TextBox38 = TextBox(new_state)

	@property
	def ShadowFlex12(self):
		self._getter_access_tracker["ShadowFlex12"] = {}
		return self._ShadowFlex12
	@ShadowFlex12.setter
	def ShadowFlex12(self, new_state):
		self._setter_access_tracker["ShadowFlex12"] = {}
		self._ShadowFlex12 = ShadowFlex(new_state)

	@property
	def FramerFlex23(self):
		self._getter_access_tracker["FramerFlex23"] = {}
		return self._FramerFlex23
	@FramerFlex23.setter
	def FramerFlex23(self, new_state):
		self._setter_access_tracker["FramerFlex23"] = {}
		self._FramerFlex23 = FramerFlex(new_state)

	@property
	def FramerFlex24(self):
		self._getter_access_tracker["FramerFlex24"] = {}
		return self._FramerFlex24
	@FramerFlex24.setter
	def FramerFlex24(self, new_state):
		self._setter_access_tracker["FramerFlex24"] = {}
		self._FramerFlex24 = FramerFlex(new_state)

	@property
	def TextBox39(self):
		self._getter_access_tracker["TextBox39"] = {}
		return self._TextBox39
	@TextBox39.setter
	def TextBox39(self, new_state):
		self._setter_access_tracker["TextBox39"] = {}
		self._TextBox39 = TextBox(new_state)

	@property
	def ShadowFlex13(self):
		self._getter_access_tracker["ShadowFlex13"] = {}
		return self._ShadowFlex13
	@ShadowFlex13.setter
	def ShadowFlex13(self, new_state):
		self._setter_access_tracker["ShadowFlex13"] = {}
		self._ShadowFlex13 = ShadowFlex(new_state)

	@property
	def Flex27(self):
		self._getter_access_tracker["Flex27"] = {}
		return self._Flex27
	@Flex27.setter
	def Flex27(self, new_state):
		self._setter_access_tracker["Flex27"] = {}
		self._Flex27 = Flex(new_state)

	@property
	def Flex28(self):
		self._getter_access_tracker["Flex28"] = {}
		return self._Flex28
	@Flex28.setter
	def Flex28(self, new_state):
		self._setter_access_tracker["Flex28"] = {}
		self._Flex28 = Flex(new_state)

	@property
	def TextBox40(self):
		self._getter_access_tracker["TextBox40"] = {}
		return self._TextBox40
	@TextBox40.setter
	def TextBox40(self, new_state):
		self._setter_access_tracker["TextBox40"] = {}
		self._TextBox40 = TextBox(new_state)

	@property
	def FramerFlex25(self):
		self._getter_access_tracker["FramerFlex25"] = {}
		return self._FramerFlex25
	@FramerFlex25.setter
	def FramerFlex25(self, new_state):
		self._setter_access_tracker["FramerFlex25"] = {}
		self._FramerFlex25 = FramerFlex(new_state)

	@property
	def TextBox41(self):
		self._getter_access_tracker["TextBox41"] = {}
		return self._TextBox41
	@TextBox41.setter
	def TextBox41(self, new_state):
		self._setter_access_tracker["TextBox41"] = {}
		self._TextBox41 = TextBox(new_state)

	@property
	def FramerFlex26(self):
		self._getter_access_tracker["FramerFlex26"] = {}
		return self._FramerFlex26
	@FramerFlex26.setter
	def FramerFlex26(self, new_state):
		self._setter_access_tracker["FramerFlex26"] = {}
		self._FramerFlex26 = FramerFlex(new_state)

	@property
	def Flex29(self):
		self._getter_access_tracker["Flex29"] = {}
		return self._Flex29
	@Flex29.setter
	def Flex29(self, new_state):
		self._setter_access_tracker["Flex29"] = {}
		self._Flex29 = Flex(new_state)

	@property
	def Flex30(self):
		self._getter_access_tracker["Flex30"] = {}
		return self._Flex30
	@Flex30.setter
	def Flex30(self, new_state):
		self._setter_access_tracker["Flex30"] = {}
		self._Flex30 = Flex(new_state)

	@property
	def TextBox42(self):
		self._getter_access_tracker["TextBox42"] = {}
		return self._TextBox42
	@TextBox42.setter
	def TextBox42(self, new_state):
		self._setter_access_tracker["TextBox42"] = {}
		self._TextBox42 = TextBox(new_state)

	@property
	def FramerFlex27(self):
		self._getter_access_tracker["FramerFlex27"] = {}
		return self._FramerFlex27
	@FramerFlex27.setter
	def FramerFlex27(self, new_state):
		self._setter_access_tracker["FramerFlex27"] = {}
		self._FramerFlex27 = FramerFlex(new_state)

	@property
	def TextBox43(self):
		self._getter_access_tracker["TextBox43"] = {}
		return self._TextBox43
	@TextBox43.setter
	def TextBox43(self, new_state):
		self._setter_access_tracker["TextBox43"] = {}
		self._TextBox43 = TextBox(new_state)

	@property
	def ShadowFlex14(self):
		self._getter_access_tracker["ShadowFlex14"] = {}
		return self._ShadowFlex14
	@ShadowFlex14.setter
	def ShadowFlex14(self, new_state):
		self._setter_access_tracker["ShadowFlex14"] = {}
		self._ShadowFlex14 = ShadowFlex(new_state)

	@property
	def FramerFlex28(self):
		self._getter_access_tracker["FramerFlex28"] = {}
		return self._FramerFlex28
	@FramerFlex28.setter
	def FramerFlex28(self, new_state):
		self._setter_access_tracker["FramerFlex28"] = {}
		self._FramerFlex28 = FramerFlex(new_state)

	@property
	def Flex31(self):
		self._getter_access_tracker["Flex31"] = {}
		return self._Flex31
	@Flex31.setter
	def Flex31(self, new_state):
		self._setter_access_tracker["Flex31"] = {}
		self._Flex31 = Flex(new_state)

	@property
	def FramerFlex29(self):
		self._getter_access_tracker["FramerFlex29"] = {}
		return self._FramerFlex29
	@FramerFlex29.setter
	def FramerFlex29(self, new_state):
		self._setter_access_tracker["FramerFlex29"] = {}
		self._FramerFlex29 = FramerFlex(new_state)

	@property
	def Image4(self):
		self._getter_access_tracker["Image4"] = {}
		return self._Image4
	@Image4.setter
	def Image4(self, new_state):
		self._setter_access_tracker["Image4"] = {}
		self._Image4 = Image(new_state)

	@property
	def Image5(self):
		self._getter_access_tracker["Image5"] = {}
		return self._Image5
	@Image5.setter
	def Image5(self, new_state):
		self._setter_access_tracker["Image5"] = {}
		self._Image5 = Image(new_state)

	@property
	def FramerFlex30(self):
		self._getter_access_tracker["FramerFlex30"] = {}
		return self._FramerFlex30
	@FramerFlex30.setter
	def FramerFlex30(self, new_state):
		self._setter_access_tracker["FramerFlex30"] = {}
		self._FramerFlex30 = FramerFlex(new_state)

	@property
	def Image6(self):
		self._getter_access_tracker["Image6"] = {}
		return self._Image6
	@Image6.setter
	def Image6(self, new_state):
		self._setter_access_tracker["Image6"] = {}
		self._Image6 = Image(new_state)

	@property
	def FramerFlex31(self):
		self._getter_access_tracker["FramerFlex31"] = {}
		return self._FramerFlex31
	@FramerFlex31.setter
	def FramerFlex31(self, new_state):
		self._setter_access_tracker["FramerFlex31"] = {}
		self._FramerFlex31 = FramerFlex(new_state)

	@property
	def Image7(self):
		self._getter_access_tracker["Image7"] = {}
		return self._Image7
	@Image7.setter
	def Image7(self, new_state):
		self._setter_access_tracker["Image7"] = {}
		self._Image7 = Image(new_state)

	@property
	def FramerFlex32(self):
		self._getter_access_tracker["FramerFlex32"] = {}
		return self._FramerFlex32
	@FramerFlex32.setter
	def FramerFlex32(self, new_state):
		self._setter_access_tracker["FramerFlex32"] = {}
		self._FramerFlex32 = FramerFlex(new_state)

	@property
	def Image8(self):
		self._getter_access_tracker["Image8"] = {}
		return self._Image8
	@Image8.setter
	def Image8(self, new_state):
		self._setter_access_tracker["Image8"] = {}
		self._Image8 = Image(new_state)

	@property
	def FramerFlex33(self):
		self._getter_access_tracker["FramerFlex33"] = {}
		return self._FramerFlex33
	@FramerFlex33.setter
	def FramerFlex33(self, new_state):
		self._setter_access_tracker["FramerFlex33"] = {}
		self._FramerFlex33 = FramerFlex(new_state)

	@property
	def Image9(self):
		self._getter_access_tracker["Image9"] = {}
		return self._Image9
	@Image9.setter
	def Image9(self, new_state):
		self._setter_access_tracker["Image9"] = {}
		self._Image9 = Image(new_state)

	@property
	def FramerFlex34(self):
		self._getter_access_tracker["FramerFlex34"] = {}
		return self._FramerFlex34
	@FramerFlex34.setter
	def FramerFlex34(self, new_state):
		self._setter_access_tracker["FramerFlex34"] = {}
		self._FramerFlex34 = FramerFlex(new_state)

	@property
	def Flex32(self):
		self._getter_access_tracker["Flex32"] = {}
		return self._Flex32
	@Flex32.setter
	def Flex32(self, new_state):
		self._setter_access_tracker["Flex32"] = {}
		self._Flex32 = Flex(new_state)

	@property
	def Flex33(self):
		self._getter_access_tracker["Flex33"] = {}
		return self._Flex33
	@Flex33.setter
	def Flex33(self, new_state):
		self._setter_access_tracker["Flex33"] = {}
		self._Flex33 = Flex(new_state)

	@property
	def TextBox44(self):
		self._getter_access_tracker["TextBox44"] = {}
		return self._TextBox44
	@TextBox44.setter
	def TextBox44(self, new_state):
		self._setter_access_tracker["TextBox44"] = {}
		self._TextBox44 = TextBox(new_state)

	@property
	def TextBox45(self):
		self._getter_access_tracker["TextBox45"] = {}
		return self._TextBox45
	@TextBox45.setter
	def TextBox45(self, new_state):
		self._setter_access_tracker["TextBox45"] = {}
		self._TextBox45 = TextBox(new_state)

	@property
	def FramerFlex35(self):
		self._getter_access_tracker["FramerFlex35"] = {}
		return self._FramerFlex35
	@FramerFlex35.setter
	def FramerFlex35(self, new_state):
		self._setter_access_tracker["FramerFlex35"] = {}
		self._FramerFlex35 = FramerFlex(new_state)

	@property
	def FramerFlex36(self):
		self._getter_access_tracker["FramerFlex36"] = {}
		return self._FramerFlex36
	@FramerFlex36.setter
	def FramerFlex36(self, new_state):
		self._setter_access_tracker["FramerFlex36"] = {}
		self._FramerFlex36 = FramerFlex(new_state)

	@property
	def Flex34(self):
		self._getter_access_tracker["Flex34"] = {}
		return self._Flex34
	@Flex34.setter
	def Flex34(self, new_state):
		self._setter_access_tracker["Flex34"] = {}
		self._Flex34 = Flex(new_state)

	@property
	def Flex35(self):
		self._getter_access_tracker["Flex35"] = {}
		return self._Flex35
	@Flex35.setter
	def Flex35(self, new_state):
		self._setter_access_tracker["Flex35"] = {}
		self._Flex35 = Flex(new_state)

	@property
	def FramerFlex37(self):
		self._getter_access_tracker["FramerFlex37"] = {}
		return self._FramerFlex37
	@FramerFlex37.setter
	def FramerFlex37(self, new_state):
		self._setter_access_tracker["FramerFlex37"] = {}
		self._FramerFlex37 = FramerFlex(new_state)

	@property
	def ShadowFlex15(self):
		self._getter_access_tracker["ShadowFlex15"] = {}
		return self._ShadowFlex15
	@ShadowFlex15.setter
	def ShadowFlex15(self, new_state):
		self._setter_access_tracker["ShadowFlex15"] = {}
		self._ShadowFlex15 = ShadowFlex(new_state)

	@property
	def Image10(self):
		self._getter_access_tracker["Image10"] = {}
		return self._Image10
	@Image10.setter
	def Image10(self, new_state):
		self._setter_access_tracker["Image10"] = {}
		self._Image10 = Image(new_state)

	@property
	def Flex36(self):
		self._getter_access_tracker["Flex36"] = {}
		return self._Flex36
	@Flex36.setter
	def Flex36(self, new_state):
		self._setter_access_tracker["Flex36"] = {}
		self._Flex36 = Flex(new_state)

	@property
	def Flex37(self):
		self._getter_access_tracker["Flex37"] = {}
		return self._Flex37
	@Flex37.setter
	def Flex37(self, new_state):
		self._setter_access_tracker["Flex37"] = {}
		self._Flex37 = Flex(new_state)

	@property
	def Flex38(self):
		self._getter_access_tracker["Flex38"] = {}
		return self._Flex38
	@Flex38.setter
	def Flex38(self, new_state):
		self._setter_access_tracker["Flex38"] = {}
		self._Flex38 = Flex(new_state)

	@property
	def TextBox46(self):
		self._getter_access_tracker["TextBox46"] = {}
		return self._TextBox46
	@TextBox46.setter
	def TextBox46(self, new_state):
		self._setter_access_tracker["TextBox46"] = {}
		self._TextBox46 = TextBox(new_state)

	@property
	def TextBox47(self):
		self._getter_access_tracker["TextBox47"] = {}
		return self._TextBox47
	@TextBox47.setter
	def TextBox47(self, new_state):
		self._setter_access_tracker["TextBox47"] = {}
		self._TextBox47 = TextBox(new_state)

	@property
	def Image11(self):
		self._getter_access_tracker["Image11"] = {}
		return self._Image11
	@Image11.setter
	def Image11(self, new_state):
		self._setter_access_tracker["Image11"] = {}
		self._Image11 = Image(new_state)

	@property
	def Flex39(self):
		self._getter_access_tracker["Flex39"] = {}
		return self._Flex39
	@Flex39.setter
	def Flex39(self, new_state):
		self._setter_access_tracker["Flex39"] = {}
		self._Flex39 = Flex(new_state)

	@property
	def TextBox48(self):
		self._getter_access_tracker["TextBox48"] = {}
		return self._TextBox48
	@TextBox48.setter
	def TextBox48(self, new_state):
		self._setter_access_tracker["TextBox48"] = {}
		self._TextBox48 = TextBox(new_state)

	@property
	def TextBox49(self):
		self._getter_access_tracker["TextBox49"] = {}
		return self._TextBox49
	@TextBox49.setter
	def TextBox49(self, new_state):
		self._setter_access_tracker["TextBox49"] = {}
		self._TextBox49 = TextBox(new_state)

	@property
	def TextBox50(self):
		self._getter_access_tracker["TextBox50"] = {}
		return self._TextBox50
	@TextBox50.setter
	def TextBox50(self, new_state):
		self._setter_access_tracker["TextBox50"] = {}
		self._TextBox50 = TextBox(new_state)

	@property
	def TextBox51(self):
		self._getter_access_tracker["TextBox51"] = {}
		return self._TextBox51
	@TextBox51.setter
	def TextBox51(self, new_state):
		self._setter_access_tracker["TextBox51"] = {}
		self._TextBox51 = TextBox(new_state)

	@property
	def TextBox52(self):
		self._getter_access_tracker["TextBox52"] = {}
		return self._TextBox52
	@TextBox52.setter
	def TextBox52(self, new_state):
		self._setter_access_tracker["TextBox52"] = {}
		self._TextBox52 = TextBox(new_state)

	@property
	def TextBox53(self):
		self._getter_access_tracker["TextBox53"] = {}
		return self._TextBox53
	@TextBox53.setter
	def TextBox53(self, new_state):
		self._setter_access_tracker["TextBox53"] = {}
		self._TextBox53 = TextBox(new_state)

	@property
	def Flex40(self):
		self._getter_access_tracker["Flex40"] = {}
		return self._Flex40
	@Flex40.setter
	def Flex40(self, new_state):
		self._setter_access_tracker["Flex40"] = {}
		self._Flex40 = Flex(new_state)

	@property
	def Image12(self):
		self._getter_access_tracker["Image12"] = {}
		return self._Image12
	@Image12.setter
	def Image12(self, new_state):
		self._setter_access_tracker["Image12"] = {}
		self._Image12 = Image(new_state)

	@property
	def Flex41(self):
		self._getter_access_tracker["Flex41"] = {}
		return self._Flex41
	@Flex41.setter
	def Flex41(self, new_state):
		self._setter_access_tracker["Flex41"] = {}
		self._Flex41 = Flex(new_state)

	@property
	def Flex42(self):
		self._getter_access_tracker["Flex42"] = {}
		return self._Flex42
	@Flex42.setter
	def Flex42(self, new_state):
		self._setter_access_tracker["Flex42"] = {}
		self._Flex42 = Flex(new_state)

	@property
	def Flex43(self):
		self._getter_access_tracker["Flex43"] = {}
		return self._Flex43
	@Flex43.setter
	def Flex43(self, new_state):
		self._setter_access_tracker["Flex43"] = {}
		self._Flex43 = Flex(new_state)

	@property
	def Image13(self):
		self._getter_access_tracker["Image13"] = {}
		return self._Image13
	@Image13.setter
	def Image13(self, new_state):
		self._setter_access_tracker["Image13"] = {}
		self._Image13 = Image(new_state)

	@property
	def ShadowFlex16(self):
		self._getter_access_tracker["ShadowFlex16"] = {}
		return self._ShadowFlex16
	@ShadowFlex16.setter
	def ShadowFlex16(self, new_state):
		self._setter_access_tracker["ShadowFlex16"] = {}
		self._ShadowFlex16 = ShadowFlex(new_state)

	@property
	def FramerFlex38(self):
		self._getter_access_tracker["FramerFlex38"] = {}
		return self._FramerFlex38
	@FramerFlex38.setter
	def FramerFlex38(self, new_state):
		self._setter_access_tracker["FramerFlex38"] = {}
		self._FramerFlex38 = FramerFlex(new_state)

	@property
	def TextBox54(self):
		self._getter_access_tracker["TextBox54"] = {}
		return self._TextBox54
	@TextBox54.setter
	def TextBox54(self, new_state):
		self._setter_access_tracker["TextBox54"] = {}
		self._TextBox54 = TextBox(new_state)

	@property
	def TextBox55(self):
		self._getter_access_tracker["TextBox55"] = {}
		return self._TextBox55
	@TextBox55.setter
	def TextBox55(self, new_state):
		self._setter_access_tracker["TextBox55"] = {}
		self._TextBox55 = TextBox(new_state)

	@property
	def TextBox56(self):
		self._getter_access_tracker["TextBox56"] = {}
		return self._TextBox56
	@TextBox56.setter
	def TextBox56(self, new_state):
		self._setter_access_tracker["TextBox56"] = {}
		self._TextBox56 = TextBox(new_state)

	@property
	def TextBox57(self):
		self._getter_access_tracker["TextBox57"] = {}
		return self._TextBox57
	@TextBox57.setter
	def TextBox57(self, new_state):
		self._setter_access_tracker["TextBox57"] = {}
		self._TextBox57 = TextBox(new_state)

	@property
	def Flex44(self):
		self._getter_access_tracker["Flex44"] = {}
		return self._Flex44
	@Flex44.setter
	def Flex44(self, new_state):
		self._setter_access_tracker["Flex44"] = {}
		self._Flex44 = Flex(new_state)

	@property
	def Image14(self):
		self._getter_access_tracker["Image14"] = {}
		return self._Image14
	@Image14.setter
	def Image14(self, new_state):
		self._setter_access_tracker["Image14"] = {}
		self._Image14 = Image(new_state)

	@property
	def Flex45(self):
		self._getter_access_tracker["Flex45"] = {}
		return self._Flex45
	@Flex45.setter
	def Flex45(self, new_state):
		self._setter_access_tracker["Flex45"] = {}
		self._Flex45 = Flex(new_state)

	@property
	def Flex46(self):
		self._getter_access_tracker["Flex46"] = {}
		return self._Flex46
	@Flex46.setter
	def Flex46(self, new_state):
		self._setter_access_tracker["Flex46"] = {}
		self._Flex46 = Flex(new_state)

	@property
	def Flex47(self):
		self._getter_access_tracker["Flex47"] = {}
		return self._Flex47
	@Flex47.setter
	def Flex47(self, new_state):
		self._setter_access_tracker["Flex47"] = {}
		self._Flex47 = Flex(new_state)

	@property
	def Image15(self):
		self._getter_access_tracker["Image15"] = {}
		return self._Image15
	@Image15.setter
	def Image15(self, new_state):
		self._setter_access_tracker["Image15"] = {}
		self._Image15 = Image(new_state)

	@property
	def ShadowFlex17(self):
		self._getter_access_tracker["ShadowFlex17"] = {}
		return self._ShadowFlex17
	@ShadowFlex17.setter
	def ShadowFlex17(self, new_state):
		self._setter_access_tracker["ShadowFlex17"] = {}
		self._ShadowFlex17 = ShadowFlex(new_state)

	@property
	def FramerFlex39(self):
		self._getter_access_tracker["FramerFlex39"] = {}
		return self._FramerFlex39
	@FramerFlex39.setter
	def FramerFlex39(self, new_state):
		self._setter_access_tracker["FramerFlex39"] = {}
		self._FramerFlex39 = FramerFlex(new_state)

	@property
	def Anchor10(self):
		self._getter_access_tracker["Anchor10"] = {}
		return self._Anchor10
	@Anchor10.setter
	def Anchor10(self, new_state):
		self._setter_access_tracker["Anchor10"] = {}
		self._Anchor10 = Anchor(new_state)

	@property
	def Anchor11(self):
		self._getter_access_tracker["Anchor11"] = {}
		return self._Anchor11
	@Anchor11.setter
	def Anchor11(self, new_state):
		self._setter_access_tracker["Anchor11"] = {}
		self._Anchor11 = Anchor(new_state)

	@property
	def Anchor12(self):
		self._getter_access_tracker["Anchor12"] = {}
		return self._Anchor12
	@Anchor12.setter
	def Anchor12(self, new_state):
		self._setter_access_tracker["Anchor12"] = {}
		self._Anchor12 = Anchor(new_state)

	@property
	def TextBox58(self):
		self._getter_access_tracker["TextBox58"] = {}
		return self._TextBox58
	@TextBox58.setter
	def TextBox58(self, new_state):
		self._setter_access_tracker["TextBox58"] = {}
		self._TextBox58 = TextBox(new_state)

	@property
	def ShadowFlex18(self):
		self._getter_access_tracker["ShadowFlex18"] = {}
		return self._ShadowFlex18
	@ShadowFlex18.setter
	def ShadowFlex18(self, new_state):
		self._setter_access_tracker["ShadowFlex18"] = {}
		self._ShadowFlex18 = ShadowFlex(new_state)

	@property
	def FramerFlex40(self):
		self._getter_access_tracker["FramerFlex40"] = {}
		return self._FramerFlex40
	@FramerFlex40.setter
	def FramerFlex40(self, new_state):
		self._setter_access_tracker["FramerFlex40"] = {}
		self._FramerFlex40 = FramerFlex(new_state)

	@property
	def Flex48(self):
		self._getter_access_tracker["Flex48"] = {}
		return self._Flex48
	@Flex48.setter
	def Flex48(self, new_state):
		self._setter_access_tracker["Flex48"] = {}
		self._Flex48 = Flex(new_state)

	@property
	def Anchor13(self):
		self._getter_access_tracker["Anchor13"] = {}
		return self._Anchor13
	@Anchor13.setter
	def Anchor13(self, new_state):
		self._setter_access_tracker["Anchor13"] = {}
		self._Anchor13 = Anchor(new_state)

	@property
	def Anchor14(self):
		self._getter_access_tracker["Anchor14"] = {}
		return self._Anchor14
	@Anchor14.setter
	def Anchor14(self, new_state):
		self._setter_access_tracker["Anchor14"] = {}
		self._Anchor14 = Anchor(new_state)

	@property
	def Anchor15(self):
		self._getter_access_tracker["Anchor15"] = {}
		return self._Anchor15
	@Anchor15.setter
	def Anchor15(self, new_state):
		self._setter_access_tracker["Anchor15"] = {}
		self._Anchor15 = Anchor(new_state)

	@property
	def Flex49(self):
		self._getter_access_tracker["Flex49"] = {}
		return self._Flex49
	@Flex49.setter
	def Flex49(self, new_state):
		self._setter_access_tracker["Flex49"] = {}
		self._Flex49 = Flex(new_state)

	@property
	def Flex50(self):
		self._getter_access_tracker["Flex50"] = {}
		return self._Flex50
	@Flex50.setter
	def Flex50(self, new_state):
		self._setter_access_tracker["Flex50"] = {}
		self._Flex50 = Flex(new_state)

	@property
	def Flex51(self):
		self._getter_access_tracker["Flex51"] = {}
		return self._Flex51
	@Flex51.setter
	def Flex51(self, new_state):
		self._setter_access_tracker["Flex51"] = {}
		self._Flex51 = Flex(new_state)

	@property
	def Flex52(self):
		self._getter_access_tracker["Flex52"] = {}
		return self._Flex52
	@Flex52.setter
	def Flex52(self, new_state):
		self._setter_access_tracker["Flex52"] = {}
		self._Flex52 = Flex(new_state)

	@property
	def Flex53(self):
		self._getter_access_tracker["Flex53"] = {}
		return self._Flex53
	@Flex53.setter
	def Flex53(self, new_state):
		self._setter_access_tracker["Flex53"] = {}
		self._Flex53 = Flex(new_state)

	@property
	def Flex54(self):
		self._getter_access_tracker["Flex54"] = {}
		return self._Flex54
	@Flex54.setter
	def Flex54(self, new_state):
		self._setter_access_tracker["Flex54"] = {}
		self._Flex54 = Flex(new_state)

	@property
	def Image16(self):
		self._getter_access_tracker["Image16"] = {}
		return self._Image16
	@Image16.setter
	def Image16(self, new_state):
		self._setter_access_tracker["Image16"] = {}
		self._Image16 = Image(new_state)

	@property
	def TextBox59(self):
		self._getter_access_tracker["TextBox59"] = {}
		return self._TextBox59
	@TextBox59.setter
	def TextBox59(self, new_state):
		self._setter_access_tracker["TextBox59"] = {}
		self._TextBox59 = TextBox(new_state)

	@property
	def Flex55(self):
		self._getter_access_tracker["Flex55"] = {}
		return self._Flex55
	@Flex55.setter
	def Flex55(self, new_state):
		self._setter_access_tracker["Flex55"] = {}
		self._Flex55 = Flex(new_state)

	@property
	def Flex56(self):
		self._getter_access_tracker["Flex56"] = {}
		return self._Flex56
	@Flex56.setter
	def Flex56(self, new_state):
		self._setter_access_tracker["Flex56"] = {}
		self._Flex56 = Flex(new_state)

	@property
	def TextBox60(self):
		self._getter_access_tracker["TextBox60"] = {}
		return self._TextBox60
	@TextBox60.setter
	def TextBox60(self, new_state):
		self._setter_access_tracker["TextBox60"] = {}
		self._TextBox60 = TextBox(new_state)

	@property
	def Input1(self):
		self._getter_access_tracker["Input1"] = {}
		return self._Input1
	@Input1.setter
	def Input1(self, new_state):
		self._setter_access_tracker["Input1"] = {}
		self._Input1 = Input(new_state)

	@property
	def TextBox61(self):
		self._getter_access_tracker["TextBox61"] = {}
		return self._TextBox61
	@TextBox61.setter
	def TextBox61(self, new_state):
		self._setter_access_tracker["TextBox61"] = {}
		self._TextBox61 = TextBox(new_state)

	@property
	def ShadowFlex19(self):
		self._getter_access_tracker["ShadowFlex19"] = {}
		return self._ShadowFlex19
	@ShadowFlex19.setter
	def ShadowFlex19(self, new_state):
		self._setter_access_tracker["ShadowFlex19"] = {}
		self._ShadowFlex19 = ShadowFlex(new_state)

	@property
	def Flex57(self):
		self._getter_access_tracker["Flex57"] = {}
		return self._Flex57
	@Flex57.setter
	def Flex57(self, new_state):
		self._setter_access_tracker["Flex57"] = {}
		self._Flex57 = Flex(new_state)

	@property
	def Flex58(self):
		self._getter_access_tracker["Flex58"] = {}
		return self._Flex58
	@Flex58.setter
	def Flex58(self, new_state):
		self._setter_access_tracker["Flex58"] = {}
		self._Flex58 = Flex(new_state)

	@property
	def TextBox62(self):
		self._getter_access_tracker["TextBox62"] = {}
		return self._TextBox62
	@TextBox62.setter
	def TextBox62(self, new_state):
		self._setter_access_tracker["TextBox62"] = {}
		self._TextBox62 = TextBox(new_state)

	@property
	def TextBox63(self):
		self._getter_access_tracker["TextBox63"] = {}
		return self._TextBox63
	@TextBox63.setter
	def TextBox63(self, new_state):
		self._setter_access_tracker["TextBox63"] = {}
		self._TextBox63 = TextBox(new_state)

	@property
	def Flex59(self):
		self._getter_access_tracker["Flex59"] = {}
		return self._Flex59
	@Flex59.setter
	def Flex59(self, new_state):
		self._setter_access_tracker["Flex59"] = {}
		self._Flex59 = Flex(new_state)

	@property
	def Flex60(self):
		self._getter_access_tracker["Flex60"] = {}
		return self._Flex60
	@Flex60.setter
	def Flex60(self, new_state):
		self._setter_access_tracker["Flex60"] = {}
		self._Flex60 = Flex(new_state)

	@property
	def TextBox64(self):
		self._getter_access_tracker["TextBox64"] = {}
		return self._TextBox64
	@TextBox64.setter
	def TextBox64(self, new_state):
		self._setter_access_tracker["TextBox64"] = {}
		self._TextBox64 = TextBox(new_state)

	@property
	def TextBox65(self):
		self._getter_access_tracker["TextBox65"] = {}
		return self._TextBox65
	@TextBox65.setter
	def TextBox65(self, new_state):
		self._setter_access_tracker["TextBox65"] = {}
		self._TextBox65 = TextBox(new_state)

	@property
	def TextBox66(self):
		self._getter_access_tracker["TextBox66"] = {}
		return self._TextBox66
	@TextBox66.setter
	def TextBox66(self, new_state):
		self._setter_access_tracker["TextBox66"] = {}
		self._TextBox66 = TextBox(new_state)

	@property
	def TextBox67(self):
		self._getter_access_tracker["TextBox67"] = {}
		return self._TextBox67
	@TextBox67.setter
	def TextBox67(self, new_state):
		self._setter_access_tracker["TextBox67"] = {}
		self._TextBox67 = TextBox(new_state)

	@property
	def TextBox68(self):
		self._getter_access_tracker["TextBox68"] = {}
		return self._TextBox68
	@TextBox68.setter
	def TextBox68(self, new_state):
		self._setter_access_tracker["TextBox68"] = {}
		self._TextBox68 = TextBox(new_state)

	@property
	def TextBox69(self):
		self._getter_access_tracker["TextBox69"] = {}
		return self._TextBox69
	@TextBox69.setter
	def TextBox69(self, new_state):
		self._setter_access_tracker["TextBox69"] = {}
		self._TextBox69 = TextBox(new_state)

	@property
	def TextBox70(self):
		self._getter_access_tracker["TextBox70"] = {}
		return self._TextBox70
	@TextBox70.setter
	def TextBox70(self, new_state):
		self._setter_access_tracker["TextBox70"] = {}
		self._TextBox70 = TextBox(new_state)

	@property
	def Anchor16(self):
		self._getter_access_tracker["Anchor16"] = {}
		return self._Anchor16
	@Anchor16.setter
	def Anchor16(self, new_state):
		self._setter_access_tracker["Anchor16"] = {}
		self._Anchor16 = Anchor(new_state)

	@property
	def Anchor17(self):
		self._getter_access_tracker["Anchor17"] = {}
		return self._Anchor17
	@Anchor17.setter
	def Anchor17(self, new_state):
		self._setter_access_tracker["Anchor17"] = {}
		self._Anchor17 = Anchor(new_state)

	@property
	def Anchor18(self):
		self._getter_access_tracker["Anchor18"] = {}
		return self._Anchor18
	@Anchor18.setter
	def Anchor18(self, new_state):
		self._setter_access_tracker["Anchor18"] = {}
		self._Anchor18 = Anchor(new_state)

	@property
	def Anchor19(self):
		self._getter_access_tracker["Anchor19"] = {}
		return self._Anchor19
	@Anchor19.setter
	def Anchor19(self, new_state):
		self._setter_access_tracker["Anchor19"] = {}
		self._Anchor19 = Anchor(new_state)

	@property
	def Anchor20(self):
		self._getter_access_tracker["Anchor20"] = {}
		return self._Anchor20
	@Anchor20.setter
	def Anchor20(self, new_state):
		self._setter_access_tracker["Anchor20"] = {}
		self._Anchor20 = Anchor(new_state)

	@property
	def Anchor21(self):
		self._getter_access_tracker["Anchor21"] = {}
		return self._Anchor21
	@Anchor21.setter
	def Anchor21(self, new_state):
		self._setter_access_tracker["Anchor21"] = {}
		self._Anchor21 = Anchor(new_state)

	@property
	def Anchor22(self):
		self._getter_access_tracker["Anchor22"] = {}
		return self._Anchor22
	@Anchor22.setter
	def Anchor22(self, new_state):
		self._setter_access_tracker["Anchor22"] = {}
		self._Anchor22 = Anchor(new_state)

	@property
	def NavFlex5(self):
		self._getter_access_tracker["NavFlex5"] = {}
		return self._NavFlex5
	@NavFlex5.setter
	def NavFlex5(self, new_state):
		self._setter_access_tracker["NavFlex5"] = {}
		self._NavFlex5 = NavFlex(new_state)

	@property
	def NavFlex6(self):
		self._getter_access_tracker["NavFlex6"] = {}
		return self._NavFlex6
	@NavFlex6.setter
	def NavFlex6(self, new_state):
		self._setter_access_tracker["NavFlex6"] = {}
		self._NavFlex6 = NavFlex(new_state)

	@property
	def NavFlex7(self):
		self._getter_access_tracker["NavFlex7"] = {}
		return self._NavFlex7
	@NavFlex7.setter
	def NavFlex7(self, new_state):
		self._setter_access_tracker["NavFlex7"] = {}
		self._NavFlex7 = NavFlex(new_state)

	@property
	def NavFlex8(self):
		self._getter_access_tracker["NavFlex8"] = {}
		return self._NavFlex8
	@NavFlex8.setter
	def NavFlex8(self, new_state):
		self._setter_access_tracker["NavFlex8"] = {}
		self._NavFlex8 = NavFlex(new_state)

	@property
	def NavFlex9(self):
		self._getter_access_tracker["NavFlex9"] = {}
		return self._NavFlex9
	@NavFlex9.setter
	def NavFlex9(self, new_state):
		self._setter_access_tracker["NavFlex9"] = {}
		self._NavFlex9 = NavFlex(new_state)

	@property
	def NavFlex10(self):
		self._getter_access_tracker["NavFlex10"] = {}
		return self._NavFlex10
	@NavFlex10.setter
	def NavFlex10(self, new_state):
		self._setter_access_tracker["NavFlex10"] = {}
		self._NavFlex10 = NavFlex(new_state)

	@property
	def NavFlex11(self):
		self._getter_access_tracker["NavFlex11"] = {}
		return self._NavFlex11
	@NavFlex11.setter
	def NavFlex11(self, new_state):
		self._setter_access_tracker["NavFlex11"] = {}
		self._NavFlex11 = NavFlex(new_state)

	@property
	def NavFlex12(self):
		self._getter_access_tracker["NavFlex12"] = {}
		return self._NavFlex12
	@NavFlex12.setter
	def NavFlex12(self, new_state):
		self._setter_access_tracker["NavFlex12"] = {}
		self._NavFlex12 = NavFlex(new_state)

	@property
	def Anchor23(self):
		self._getter_access_tracker["Anchor23"] = {}
		return self._Anchor23
	@Anchor23.setter
	def Anchor23(self, new_state):
		self._setter_access_tracker["Anchor23"] = {}
		self._Anchor23 = Anchor(new_state)

	@property
	def Image17(self):
		self._getter_access_tracker["Image17"] = {}
		return self._Image17
	@Image17.setter
	def Image17(self, new_state):
		self._setter_access_tracker["Image17"] = {}
		self._Image17 = Image(new_state)

	@property
	def TextBox71(self):
		self._getter_access_tracker["TextBox71"] = {}
		return self._TextBox71
	@TextBox71.setter
	def TextBox71(self, new_state):
		self._setter_access_tracker["TextBox71"] = {}
		self._TextBox71 = TextBox(new_state)

	@property
	def TextBox72(self):
		self._getter_access_tracker["TextBox72"] = {}
		return self._TextBox72
	@TextBox72.setter
	def TextBox72(self, new_state):
		self._setter_access_tracker["TextBox72"] = {}
		self._TextBox72 = TextBox(new_state)

	@property
	def Image18(self):
		self._getter_access_tracker["Image18"] = {}
		return self._Image18
	@Image18.setter
	def Image18(self, new_state):
		self._setter_access_tracker["Image18"] = {}
		self._Image18 = Image(new_state)

	@property
	def NavFlex13(self):
		self._getter_access_tracker["NavFlex13"] = {}
		return self._NavFlex13
	@NavFlex13.setter
	def NavFlex13(self, new_state):
		self._setter_access_tracker["NavFlex13"] = {}
		self._NavFlex13 = NavFlex(new_state)

	@property
	def Anchor24(self):
		self._getter_access_tracker["Anchor24"] = {}
		return self._Anchor24
	@Anchor24.setter
	def Anchor24(self, new_state):
		self._setter_access_tracker["Anchor24"] = {}
		self._Anchor24 = Anchor(new_state)

	@property
	def TextBox73(self):
		self._getter_access_tracker["TextBox73"] = {}
		return self._TextBox73
	@TextBox73.setter
	def TextBox73(self, new_state):
		self._setter_access_tracker["TextBox73"] = {}
		self._TextBox73 = TextBox(new_state)

	@property
	def Image19(self):
		self._getter_access_tracker["Image19"] = {}
		return self._Image19
	@Image19.setter
	def Image19(self, new_state):
		self._setter_access_tracker["Image19"] = {}
		self._Image19 = Image(new_state)

	@property
	def NavFlex14(self):
		self._getter_access_tracker["NavFlex14"] = {}
		return self._NavFlex14
	@NavFlex14.setter
	def NavFlex14(self, new_state):
		self._setter_access_tracker["NavFlex14"] = {}
		self._NavFlex14 = NavFlex(new_state)

	@property
	def Anchor25(self):
		self._getter_access_tracker["Anchor25"] = {}
		return self._Anchor25
	@Anchor25.setter
	def Anchor25(self, new_state):
		self._setter_access_tracker["Anchor25"] = {}
		self._Anchor25 = Anchor(new_state)

	@property
	def TextBox74(self):
		self._getter_access_tracker["TextBox74"] = {}
		return self._TextBox74
	@TextBox74.setter
	def TextBox74(self, new_state):
		self._setter_access_tracker["TextBox74"] = {}
		self._TextBox74 = TextBox(new_state)

	@property
	def Image20(self):
		self._getter_access_tracker["Image20"] = {}
		return self._Image20
	@Image20.setter
	def Image20(self, new_state):
		self._setter_access_tracker["Image20"] = {}
		self._Image20 = Image(new_state)

	@property
	def NavFlex15(self):
		self._getter_access_tracker["NavFlex15"] = {}
		return self._NavFlex15
	@NavFlex15.setter
	def NavFlex15(self, new_state):
		self._setter_access_tracker["NavFlex15"] = {}
		self._NavFlex15 = NavFlex(new_state)

	@property
	def Anchor26(self):
		self._getter_access_tracker["Anchor26"] = {}
		return self._Anchor26
	@Anchor26.setter
	def Anchor26(self, new_state):
		self._setter_access_tracker["Anchor26"] = {}
		self._Anchor26 = Anchor(new_state)

	@property
	def TextBox75(self):
		self._getter_access_tracker["TextBox75"] = {}
		return self._TextBox75
	@TextBox75.setter
	def TextBox75(self, new_state):
		self._setter_access_tracker["TextBox75"] = {}
		self._TextBox75 = TextBox(new_state)

	@property
	def Flex61(self):
		self._getter_access_tracker["Flex61"] = {}
		return self._Flex61
	@Flex61.setter
	def Flex61(self, new_state):
		self._setter_access_tracker["Flex61"] = {}
		self._Flex61 = Flex(new_state)

	@property
	def Anchor27(self):
		self._getter_access_tracker["Anchor27"] = {}
		return self._Anchor27
	@Anchor27.setter
	def Anchor27(self, new_state):
		self._setter_access_tracker["Anchor27"] = {}
		self._Anchor27 = Anchor(new_state)

	@property
	def NavFlex16(self):
		self._getter_access_tracker["NavFlex16"] = {}
		return self._NavFlex16
	@NavFlex16.setter
	def NavFlex16(self, new_state):
		self._setter_access_tracker["NavFlex16"] = {}
		self._NavFlex16 = NavFlex(new_state)

	@property
	def TextBox77(self):
		self._getter_access_tracker["TextBox77"] = {}
		return self._TextBox77
	@TextBox77.setter
	def TextBox77(self, new_state):
		self._setter_access_tracker["TextBox77"] = {}
		self._TextBox77 = TextBox(new_state)

	@property
	def TextBox78(self):
		self._getter_access_tracker["TextBox78"] = {}
		return self._TextBox78
	@TextBox78.setter
	def TextBox78(self, new_state):
		self._setter_access_tracker["TextBox78"] = {}
		self._TextBox78 = TextBox(new_state)

	@property
	def NavFlex17(self):
		self._getter_access_tracker["NavFlex17"] = {}
		return self._NavFlex17
	@NavFlex17.setter
	def NavFlex17(self, new_state):
		self._setter_access_tracker["NavFlex17"] = {}
		self._NavFlex17 = NavFlex(new_state)

	@property
	def Anchor28(self):
		self._getter_access_tracker["Anchor28"] = {}
		return self._Anchor28
	@Anchor28.setter
	def Anchor28(self, new_state):
		self._setter_access_tracker["Anchor28"] = {}
		self._Anchor28 = Anchor(new_state)

	@property
	def TextBox79(self):
		self._getter_access_tracker["TextBox79"] = {}
		return self._TextBox79
	@TextBox79.setter
	def TextBox79(self, new_state):
		self._setter_access_tracker["TextBox79"] = {}
		self._TextBox79 = TextBox(new_state)

	@property
	def NavFlex18(self):
		self._getter_access_tracker["NavFlex18"] = {}
		return self._NavFlex18
	@NavFlex18.setter
	def NavFlex18(self, new_state):
		self._setter_access_tracker["NavFlex18"] = {}
		self._NavFlex18 = NavFlex(new_state)

	@property
	def Anchor29(self):
		self._getter_access_tracker["Anchor29"] = {}
		return self._Anchor29
	@Anchor29.setter
	def Anchor29(self, new_state):
		self._setter_access_tracker["Anchor29"] = {}
		self._Anchor29 = Anchor(new_state)

	@property
	def TextBox80(self):
		self._getter_access_tracker["TextBox80"] = {}
		return self._TextBox80
	@TextBox80.setter
	def TextBox80(self, new_state):
		self._setter_access_tracker["TextBox80"] = {}
		self._TextBox80 = TextBox(new_state)

	@property
	def TextBox81(self):
		self._getter_access_tracker["TextBox81"] = {}
		return self._TextBox81
	@TextBox81.setter
	def TextBox81(self, new_state):
		self._setter_access_tracker["TextBox81"] = {}
		self._TextBox81 = TextBox(new_state)

	@property
	def TextBox82(self):
		self._getter_access_tracker["TextBox82"] = {}
		return self._TextBox82
	@TextBox82.setter
	def TextBox82(self, new_state):
		self._setter_access_tracker["TextBox82"] = {}
		self._TextBox82 = TextBox(new_state)

	@property
	def NavFlex19(self):
		self._getter_access_tracker["NavFlex19"] = {}
		return self._NavFlex19
	@NavFlex19.setter
	def NavFlex19(self, new_state):
		self._setter_access_tracker["NavFlex19"] = {}
		self._NavFlex19 = NavFlex(new_state)

	@property
	def NavFlex20(self):
		self._getter_access_tracker["NavFlex20"] = {}
		return self._NavFlex20
	@NavFlex20.setter
	def NavFlex20(self, new_state):
		self._setter_access_tracker["NavFlex20"] = {}
		self._NavFlex20 = NavFlex(new_state)

	@property
	def NavFlex21(self):
		self._getter_access_tracker["NavFlex21"] = {}
		return self._NavFlex21
	@NavFlex21.setter
	def NavFlex21(self, new_state):
		self._setter_access_tracker["NavFlex21"] = {}
		self._NavFlex21 = NavFlex(new_state)

	@property
	def Anchor30(self):
		self._getter_access_tracker["Anchor30"] = {}
		return self._Anchor30
	@Anchor30.setter
	def Anchor30(self, new_state):
		self._setter_access_tracker["Anchor30"] = {}
		self._Anchor30 = Anchor(new_state)

	@property
	def Anchor31(self):
		self._getter_access_tracker["Anchor31"] = {}
		return self._Anchor31
	@Anchor31.setter
	def Anchor31(self, new_state):
		self._setter_access_tracker["Anchor31"] = {}
		self._Anchor31 = Anchor(new_state)

	@property
	def Anchor32(self):
		self._getter_access_tracker["Anchor32"] = {}
		return self._Anchor32
	@Anchor32.setter
	def Anchor32(self, new_state):
		self._setter_access_tracker["Anchor32"] = {}
		self._Anchor32 = Anchor(new_state)

	@property
	def Flex62(self):
		self._getter_access_tracker["Flex62"] = {}
		return self._Flex62
	@Flex62.setter
	def Flex62(self, new_state):
		self._setter_access_tracker["Flex62"] = {}
		self._Flex62 = Flex(new_state)
  
	def _to_json_fields(self):
		return {
			"Flex1": self._Flex1,
			"TextBox1": self._TextBox1,
			"ShadowFlex1": self._ShadowFlex1,
			"Flex2": self._Flex2,
			"NavFlex1": self._NavFlex1,
			"TextBox2": self._TextBox2,
			"TextBox3": self._TextBox3,
			"NavFlex2": self._NavFlex2,
			"TextBox4": self._TextBox4,
			"NavFlex3": self._NavFlex3,
			"TextBox5": self._TextBox5,
			"NavFlex4": self._NavFlex4,
			"Flex4": self._Flex4,
			"Flex5": self._Flex5,
			"Flex6": self._Flex6,
			"Flex7": self._Flex7,
			"Flex8": self._Flex8,
			"Image1": self._Image1,
			"Flex9": self._Flex9,
			"Flex10": self._Flex10,
			"Anchor1": self._Anchor1,
			"Anchor2": self._Anchor2,
			"Anchor3": self._Anchor3,
			"Anchor4": self._Anchor4,
			"ShadowFlex2": self._ShadowFlex2,
			"TextBox13": self._TextBox13,
			"Anchor5": self._Anchor5,
			"TextBox14": self._TextBox14,
			"ShadowFlex3": self._ShadowFlex3,
			"Anchor6": self._Anchor6,
			"Anchor7": self._Anchor7,
			"Dropdown1": self._Dropdown1,
			"Flex11": self._Flex11,
			"Image2": self._Image2,
			"Flex12": self._Flex12,
			"Flex13": self._Flex13,
			"Flex14": self._Flex14,
			"Image3": self._Image3,
			"TextBox16": self._TextBox16,
			"FramerFlex7": self._FramerFlex7,
			"TextBox17": self._TextBox17,
			"FramerFlex8": self._FramerFlex8,
			"Anchor8": self._Anchor8,
			"FramerFlex9": self._FramerFlex9,
			"FramerFlex10": self._FramerFlex10,
			"TextBox18": self._TextBox18,
			"ShadowFlex4": self._ShadowFlex4,
			"Anchor9": self._Anchor9,
			"TextBox19": self._TextBox19,
			"TextBox20": self._TextBox20,
			"FramerFlex11": self._FramerFlex11,
			"FramerFlex12": self._FramerFlex12,
			"FramerFlex13": self._FramerFlex13,
			"Flex15": self._Flex15,
			"Flex16": self._Flex16,
			"Flex17": self._Flex17,
			"Flex18": self._Flex18,
			"Flex19": self._Flex19,
			"FramerFlex14": self._FramerFlex14,
			"TextBox21": self._TextBox21,
			"TextBox22": self._TextBox22,
			"FramerFlex15": self._FramerFlex15,
			"Flex20": self._Flex20,
			"Flex21": self._Flex21,
			"Flex22": self._Flex22,
			"Flex23": self._Flex23,
			"Flex24": self._Flex24,
			"Flex25": self._Flex25,
			"FramerFlex16": self._FramerFlex16,
			"ShadowFlex5": self._ShadowFlex5,
			"TextBox23": self._TextBox23,
			"TextBox24": self._TextBox24,
			"TextBox25": self._TextBox25,
			"TextBox26": self._TextBox26,
			"ShadowFlex6": self._ShadowFlex6,
			"FramerFlex17": self._FramerFlex17,
			"TextBox27": self._TextBox27,
			"TextBox28": self._TextBox28,
			"ShadowFlex7": self._ShadowFlex7,
			"FramerFlex18": self._FramerFlex18,
			"TextBox29": self._TextBox29,
			"TextBox30": self._TextBox30,
			"ShadowFlex8": self._ShadowFlex8,
			"FramerFlex19": self._FramerFlex19,
			"TextBox31": self._TextBox31,
			"TextBox32": self._TextBox32,
			"ShadowFlex9": self._ShadowFlex9,
			"FramerFlex20": self._FramerFlex20,
			"TextBox33": self._TextBox33,
			"TextBox34": self._TextBox34,
			"ShadowFlex10": self._ShadowFlex10,
			"FramerFlex21": self._FramerFlex21,
			"TextBox35": self._TextBox35,
			"TextBox36": self._TextBox36,
			"ShadowFlex11": self._ShadowFlex11,
			"FramerFlex22": self._FramerFlex22,
			"TextBox37": self._TextBox37,
			"TextBox38": self._TextBox38,
			"ShadowFlex12": self._ShadowFlex12,
			"FramerFlex23": self._FramerFlex23,
			"FramerFlex24": self._FramerFlex24,
			"TextBox39": self._TextBox39,
			"ShadowFlex13": self._ShadowFlex13,
			"Flex27": self._Flex27,
			"Flex28": self._Flex28,
			"TextBox40": self._TextBox40,
			"FramerFlex25": self._FramerFlex25,
			"TextBox41": self._TextBox41,
			"FramerFlex26": self._FramerFlex26,
			"Flex29": self._Flex29,
			"Flex30": self._Flex30,
			"TextBox42": self._TextBox42,
			"FramerFlex27": self._FramerFlex27,
			"TextBox43": self._TextBox43,
			"ShadowFlex14": self._ShadowFlex14,
			"FramerFlex28": self._FramerFlex28,
			"Flex31": self._Flex31,
			"FramerFlex29": self._FramerFlex29,
			"Image4": self._Image4,
			"Image5": self._Image5,
			"FramerFlex30": self._FramerFlex30,
			"Image6": self._Image6,
			"FramerFlex31": self._FramerFlex31,
			"Image7": self._Image7,
			"FramerFlex32": self._FramerFlex32,
			"Image8": self._Image8,
			"FramerFlex33": self._FramerFlex33,
			"Image9": self._Image9,
			"FramerFlex34": self._FramerFlex34,
			"Flex32": self._Flex32,
			"Flex33": self._Flex33,
			"TextBox44": self._TextBox44,
			"TextBox45": self._TextBox45,
			"FramerFlex35": self._FramerFlex35,
			"FramerFlex36": self._FramerFlex36,
			"Flex34": self._Flex34,
			"Flex35": self._Flex35,
			"FramerFlex37": self._FramerFlex37,
			"ShadowFlex15": self._ShadowFlex15,
			"Image10": self._Image10,
			"Flex36": self._Flex36,
			"Flex37": self._Flex37,
			"Flex38": self._Flex38,
			"TextBox46": self._TextBox46,
			"TextBox47": self._TextBox47,
			"Image11": self._Image11,
			"Flex39": self._Flex39,
			"TextBox48": self._TextBox48,
			"TextBox49": self._TextBox49,
			"TextBox50": self._TextBox50,
			"TextBox51": self._TextBox51,
			"TextBox52": self._TextBox52,
			"TextBox53": self._TextBox53,
			"Flex40": self._Flex40,
			"Image12": self._Image12,
			"Flex41": self._Flex41,
			"Flex42": self._Flex42,
			"Flex43": self._Flex43,
			"Image13": self._Image13,
			"ShadowFlex16": self._ShadowFlex16,
			"FramerFlex38": self._FramerFlex38,
			"TextBox54": self._TextBox54,
			"TextBox55": self._TextBox55,
			"TextBox56": self._TextBox56,
			"TextBox57": self._TextBox57,
			"Flex44": self._Flex44,
			"Image14": self._Image14,
			"Flex45": self._Flex45,
			"Flex46": self._Flex46,
			"Flex47": self._Flex47,
			"Image15": self._Image15,
			"ShadowFlex17": self._ShadowFlex17,
			"FramerFlex39": self._FramerFlex39,
			"Anchor10": self._Anchor10,
			"Anchor11": self._Anchor11,
			"Anchor12": self._Anchor12,
			"TextBox58": self._TextBox58,
			"ShadowFlex18": self._ShadowFlex18,
			"FramerFlex40": self._FramerFlex40,
			"Flex48": self._Flex48,
			"Anchor13": self._Anchor13,
			"Anchor14": self._Anchor14,
			"Anchor15": self._Anchor15,
			"Flex49": self._Flex49,
			"Flex50": self._Flex50,
			"Flex51": self._Flex51,
			"Flex52": self._Flex52,
			"Flex53": self._Flex53,
			"Flex54": self._Flex54,
			"Image16": self._Image16,
			"TextBox59": self._TextBox59,
			"Flex55": self._Flex55,
			"Flex56": self._Flex56,
			"TextBox60": self._TextBox60,
			"Input1": self._Input1,
			"TextBox61": self._TextBox61,
			"ShadowFlex19": self._ShadowFlex19,
			"Flex57": self._Flex57,
			"Flex58": self._Flex58,
			"TextBox62": self._TextBox62,
			"TextBox63": self._TextBox63,
			"Flex59": self._Flex59,
			"Flex60": self._Flex60,
			"TextBox64": self._TextBox64,
			"TextBox65": self._TextBox65,
			"TextBox66": self._TextBox66,
			"TextBox67": self._TextBox67,
			"TextBox68": self._TextBox68,
			"TextBox69": self._TextBox69,
			"TextBox70": self._TextBox70,
			"Anchor16": self._Anchor16,
			"Anchor17": self._Anchor17,
			"Anchor18": self._Anchor18,
			"Anchor19": self._Anchor19,
			"Anchor20": self._Anchor20,
			"Anchor21": self._Anchor21,
			"Anchor22": self._Anchor22,
			"NavFlex5": self._NavFlex5,
			"NavFlex6": self._NavFlex6,
			"NavFlex7": self._NavFlex7,
			"NavFlex8": self._NavFlex8,
			"NavFlex9": self._NavFlex9,
			"NavFlex10": self._NavFlex10,
			"NavFlex11": self._NavFlex11,
			"NavFlex12": self._NavFlex12,
			"Anchor23": self._Anchor23,
			"Image17": self._Image17,
			"TextBox71": self._TextBox71,
			"TextBox72": self._TextBox72,
			"Image18": self._Image18,
			"NavFlex13": self._NavFlex13,
			"Anchor24": self._Anchor24,
			"TextBox73": self._TextBox73,
			"Image19": self._Image19,
			"NavFlex14": self._NavFlex14,
			"Anchor25": self._Anchor25,
			"TextBox74": self._TextBox74,
			"Image20": self._Image20,
			"NavFlex15": self._NavFlex15,
			"Anchor26": self._Anchor26,
			"TextBox75": self._TextBox75,
			"Flex61": self._Flex61,
			"Anchor27": self._Anchor27,
			"NavFlex16": self._NavFlex16,
			"TextBox77": self._TextBox77,
			"TextBox78": self._TextBox78,
			"NavFlex17": self._NavFlex17,
			"Anchor28": self._Anchor28,
			"TextBox79": self._TextBox79,
			"NavFlex18": self._NavFlex18,
			"Anchor29": self._Anchor29,
			"TextBox80": self._TextBox80,
			"TextBox81": self._TextBox81,
			"TextBox82": self._TextBox82,
			"NavFlex19": self._NavFlex19,
			"NavFlex20": self._NavFlex20,
			"NavFlex21": self._NavFlex21,
			"Anchor30": self._Anchor30,
			"Anchor31": self._Anchor31,
			"Anchor32": self._Anchor32,
			"Flex62": self._Flex62
			}
  