from typing import Union, Any
from atri_react.Flex import Flex
from atri_react.TextBox import TextBox
from manifests.FramerFlex import FramerFlex
from atri_react.Image import Image
from manifests.ShadowFlex import ShadowFlex
from atri_react.Anchor import Anchor
from manifests.NavFlex import NavFlex
from atri_react.Dropdown import Dropdown
from atri_react.Input import Input


  
class Page:
	def __init__(self, state: Union[Any, None]):
		self.event_data = None
		self.event_alias = None
		self._setter_access_tracker = {}
		self.Flex8 = state["Flex8"] if "Flex8" in state else None
		self.Flex9 = state["Flex9"] if "Flex9" in state else None
		self.Flex10 = state["Flex10"] if "Flex10" in state else None
		self.Flex11 = state["Flex11"] if "Flex11" in state else None
		self.TextBox7 = state["TextBox7"] if "TextBox7" in state else None
		self.FramerFlex1 = state["FramerFlex1"] if "FramerFlex1" in state else None
		self.FramerFlex2 = state["FramerFlex2"] if "FramerFlex2" in state else None
		self.TextBox8 = state["TextBox8"] if "TextBox8" in state else None
		self.Flex12 = state["Flex12"] if "Flex12" in state else None
		self.Flex13 = state["Flex13"] if "Flex13" in state else None
		self.Flex14 = state["Flex14"] if "Flex14" in state else None
		self.TextBox9 = state["TextBox9"] if "TextBox9" in state else None
		self.TextBox10 = state["TextBox10"] if "TextBox10" in state else None
		self.Flex15 = state["Flex15"] if "Flex15" in state else None
		self.TextBox11 = state["TextBox11"] if "TextBox11" in state else None
		self.TextBox12 = state["TextBox12"] if "TextBox12" in state else None
		self.Flex16 = state["Flex16"] if "Flex16" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
		self.TextBox13 = state["TextBox13"] if "TextBox13" in state else None
		self.TextBox14 = state["TextBox14"] if "TextBox14" in state else None
		self.Image4 = state["Image4"] if "Image4" in state else None
		self.Flex17 = state["Flex17"] if "Flex17" in state else None
		self.TextBox15 = state["TextBox15"] if "TextBox15" in state else None
		self.Image5 = state["Image5"] if "Image5" in state else None
		self.Flex18 = state["Flex18"] if "Flex18" in state else None
		self.ShadowFlex3 = state["ShadowFlex3"] if "ShadowFlex3" in state else None
		self.Flex19 = state["Flex19"] if "Flex19" in state else None
		self.TextBox16 = state["TextBox16"] if "TextBox16" in state else None
		self.Anchor9 = state["Anchor9"] if "Anchor9" in state else None
		self.TextBox17 = state["TextBox17"] if "TextBox17" in state else None
		self.ShadowFlex4 = state["ShadowFlex4"] if "ShadowFlex4" in state else None
		self.TextBox18 = state["TextBox18"] if "TextBox18" in state else None
		self.TextBox19 = state["TextBox19"] if "TextBox19" in state else None
		self.Image6 = state["Image6"] if "Image6" in state else None
		self.TextBox20 = state["TextBox20"] if "TextBox20" in state else None
		self.Image7 = state["Image7"] if "Image7" in state else None
		self.TextBox21 = state["TextBox21"] if "TextBox21" in state else None
		self.TextBox22 = state["TextBox22"] if "TextBox22" in state else None
		self.Image8 = state["Image8"] if "Image8" in state else None
		self.Flex20 = state["Flex20"] if "Flex20" in state else None
		self.Flex21 = state["Flex21"] if "Flex21" in state else None
		self.TextBox23 = state["TextBox23"] if "TextBox23" in state else None
		self.TextBox24 = state["TextBox24"] if "TextBox24" in state else None
		self.Flex22 = state["Flex22"] if "Flex22" in state else None
		self.Flex23 = state["Flex23"] if "Flex23" in state else None
		self.Flex24 = state["Flex24"] if "Flex24" in state else None
		self.Anchor10 = state["Anchor10"] if "Anchor10" in state else None
		self.Flex25 = state["Flex25"] if "Flex25" in state else None
		self.Flex26 = state["Flex26"] if "Flex26" in state else None
		self.Flex27 = state["Flex27"] if "Flex27" in state else None
		self.TextBox25 = state["TextBox25"] if "TextBox25" in state else None
		self.ShadowFlex5 = state["ShadowFlex5"] if "ShadowFlex5" in state else None
		self.TextBox26 = state["TextBox26"] if "TextBox26" in state else None
		self.TextBox27 = state["TextBox27"] if "TextBox27" in state else None
		self.Image9 = state["Image9"] if "Image9" in state else None
		self.TextBox28 = state["TextBox28"] if "TextBox28" in state else None
		self.Image10 = state["Image10"] if "Image10" in state else None
		self.TextBox29 = state["TextBox29"] if "TextBox29" in state else None
		self.TextBox30 = state["TextBox30"] if "TextBox30" in state else None
		self.Image11 = state["Image11"] if "Image11" in state else None
		self.Flex28 = state["Flex28"] if "Flex28" in state else None
		self.Flex29 = state["Flex29"] if "Flex29" in state else None
		self.TextBox31 = state["TextBox31"] if "TextBox31" in state else None
		self.TextBox32 = state["TextBox32"] if "TextBox32" in state else None
		self.Flex30 = state["Flex30"] if "Flex30" in state else None
		self.Flex31 = state["Flex31"] if "Flex31" in state else None
		self.Flex32 = state["Flex32"] if "Flex32" in state else None
		self.Anchor11 = state["Anchor11"] if "Anchor11" in state else None
		self.Flex33 = state["Flex33"] if "Flex33" in state else None
		self.Flex34 = state["Flex34"] if "Flex34" in state else None
		self.Flex35 = state["Flex35"] if "Flex35" in state else None
		self.FramerFlex3 = state["FramerFlex3"] if "FramerFlex3" in state else None
		self.FramerFlex4 = state["FramerFlex4"] if "FramerFlex4" in state else None
		self.FramerFlex5 = state["FramerFlex5"] if "FramerFlex5" in state else None
		self.TextBox56 = state["TextBox56"] if "TextBox56" in state else None
		self.TextBox57 = state["TextBox57"] if "TextBox57" in state else None
		self.TextBox58 = state["TextBox58"] if "TextBox58" in state else None
		self.TextBox59 = state["TextBox59"] if "TextBox59" in state else None
		self.TextBox60 = state["TextBox60"] if "TextBox60" in state else None
		self.TextBox61 = state["TextBox61"] if "TextBox61" in state else None
		self.ShadowFlex7 = state["ShadowFlex7"] if "ShadowFlex7" in state else None
		self.ShadowFlex8 = state["ShadowFlex8"] if "ShadowFlex8" in state else None
		self.NavFlex22 = state["NavFlex22"] if "NavFlex22" in state else None
		self.NavFlex23 = state["NavFlex23"] if "NavFlex23" in state else None
		self.NavFlex24 = state["NavFlex24"] if "NavFlex24" in state else None
		self.NavFlex25 = state["NavFlex25"] if "NavFlex25" in state else None
		self.Image17 = state["Image17"] if "Image17" in state else None
		self.Anchor29 = state["Anchor29"] if "Anchor29" in state else None
		self.Anchor30 = state["Anchor30"] if "Anchor30" in state else None
		self.Dropdown2 = state["Dropdown2"] if "Dropdown2" in state else None
		self.Anchor31 = state["Anchor31"] if "Anchor31" in state else None
		self.Anchor32 = state["Anchor32"] if "Anchor32" in state else None
		self.Anchor33 = state["Anchor33"] if "Anchor33" in state else None
		self.Anchor34 = state["Anchor34"] if "Anchor34" in state else None
		self.Image18 = state["Image18"] if "Image18" in state else None
		self.Anchor35 = state["Anchor35"] if "Anchor35" in state else None
		self.Flex50 = state["Flex50"] if "Flex50" in state else None
		self.Flex51 = state["Flex51"] if "Flex51" in state else None
		self.Flex52 = state["Flex52"] if "Flex52" in state else None
		self.Flex53 = state["Flex53"] if "Flex53" in state else None
		self.Flex54 = state["Flex54"] if "Flex54" in state else None
		self.Flex55 = state["Flex55"] if "Flex55" in state else None
		self.navbar2 = state["navbar2"] if "navbar2" in state else None
		self.Image19 = state["Image19"] if "Image19" in state else None
		self.TextBox62 = state["TextBox62"] if "TextBox62" in state else None
		self.Image20 = state["Image20"] if "Image20" in state else None
		self.TextBox63 = state["TextBox63"] if "TextBox63" in state else None
		self.Image21 = state["Image21"] if "Image21" in state else None
		self.TextBox64 = state["TextBox64"] if "TextBox64" in state else None
		self.TextBox65 = state["TextBox65"] if "TextBox65" in state else None
		self.Image22 = state["Image22"] if "Image22" in state else None
		self.TextBox66 = state["TextBox66"] if "TextBox66" in state else None
		self.TextBox67 = state["TextBox67"] if "TextBox67" in state else None
		self.TextBox68 = state["TextBox68"] if "TextBox68" in state else None
		self.TextBox69 = state["TextBox69"] if "TextBox69" in state else None
		self.TextBox70 = state["TextBox70"] if "TextBox70" in state else None
		self.TextBox71 = state["TextBox71"] if "TextBox71" in state else None
		self.TextBox72 = state["TextBox72"] if "TextBox72" in state else None
		self.NavFlex26 = state["NavFlex26"] if "NavFlex26" in state else None
		self.NavFlex27 = state["NavFlex27"] if "NavFlex27" in state else None
		self.NavFlex28 = state["NavFlex28"] if "NavFlex28" in state else None
		self.NavFlex29 = state["NavFlex29"] if "NavFlex29" in state else None
		self.Anchor36 = state["Anchor36"] if "Anchor36" in state else None
		self.Anchor37 = state["Anchor37"] if "Anchor37" in state else None
		self.Anchor38 = state["Anchor38"] if "Anchor38" in state else None
		self.Anchor39 = state["Anchor39"] if "Anchor39" in state else None
		self.Anchor40 = state["Anchor40"] if "Anchor40" in state else None
		self.Anchor41 = state["Anchor41"] if "Anchor41" in state else None
		self.Anchor42 = state["Anchor42"] if "Anchor42" in state else None
		self.TextBox73 = state["TextBox73"] if "TextBox73" in state else None
		self.TextBox74 = state["TextBox74"] if "TextBox74" in state else None
		self.TextBox75 = state["TextBox75"] if "TextBox75" in state else None
		self.TextBox76 = state["TextBox76"] if "TextBox76" in state else None
		self.TextBox77 = state["TextBox77"] if "TextBox77" in state else None
		self.TextBox78 = state["TextBox78"] if "TextBox78" in state else None
		self.TextBox79 = state["TextBox79"] if "TextBox79" in state else None
		self.Anchor43 = state["Anchor43"] if "Anchor43" in state else None
		self.Anchor44 = state["Anchor44"] if "Anchor44" in state else None
		self.Anchor45 = state["Anchor45"] if "Anchor45" in state else None
		self.Anchor46 = state["Anchor46"] if "Anchor46" in state else None
		self.NavFlex30 = state["NavFlex30"] if "NavFlex30" in state else None
		self.NavFlex31 = state["NavFlex31"] if "NavFlex31" in state else None
		self.NavFlex32 = state["NavFlex32"] if "NavFlex32" in state else None
		self.NavFlex33 = state["NavFlex33"] if "NavFlex33" in state else None
		self.NavFlex34 = state["NavFlex34"] if "NavFlex34" in state else None
		self.NavFlex35 = state["NavFlex35"] if "NavFlex35" in state else None
		self.NavFlex36 = state["NavFlex36"] if "NavFlex36" in state else None
		self.ShadowFlex9 = state["ShadowFlex9"] if "ShadowFlex9" in state else None
		self.Input2 = state["Input2"] if "Input2" in state else None
		self.NavFlex37 = state["NavFlex37"] if "NavFlex37" in state else None
		self.NavFlex38 = state["NavFlex38"] if "NavFlex38" in state else None
		self.NavFlex39 = state["NavFlex39"] if "NavFlex39" in state else None
		self.NavFlex40 = state["NavFlex40"] if "NavFlex40" in state else None
		self.NavFlex41 = state["NavFlex41"] if "NavFlex41" in state else None
		self.NavFlex42 = state["NavFlex42"] if "NavFlex42" in state else None
		self.Flex57 = state["Flex57"] if "Flex57" in state else None
		self.TextBox80 = state["TextBox80"] if "TextBox80" in state else None
		self.Flex58 = state["Flex58"] if "Flex58" in state else None
		self.TextBox81 = state["TextBox81"] if "TextBox81" in state else None
		self.TextBox82 = state["TextBox82"] if "TextBox82" in state else None
		self.Flex59 = state["Flex59"] if "Flex59" in state else None
		self.Anchor47 = state["Anchor47"] if "Anchor47" in state else None
		self.Anchor48 = state["Anchor48"] if "Anchor48" in state else None
		self.Anchor49 = state["Anchor49"] if "Anchor49" in state else None
		self.Anchor50 = state["Anchor50"] if "Anchor50" in state else None
		self.Anchor51 = state["Anchor51"] if "Anchor51" in state else None
		self.Anchor52 = state["Anchor52"] if "Anchor52" in state else None
		self.Flex60 = state["Flex60"] if "Flex60" in state else None
		self.Flex61 = state["Flex61"] if "Flex61" in state else None
		self.Flex62 = state["Flex62"] if "Flex62" in state else None
		self.TextBox83 = state["TextBox83"] if "TextBox83" in state else None
		self.Image23 = state["Image23"] if "Image23" in state else None
		self.Flex63 = state["Flex63"] if "Flex63" in state else None
		self.Flex64 = state["Flex64"] if "Flex64" in state else None
		self.TextBox84 = state["TextBox84"] if "TextBox84" in state else None
		self.Flex65 = state["Flex65"] if "Flex65" in state else None
		self.Flex66 = state["Flex66"] if "Flex66" in state else None
		self.Flex67 = state["Flex67"] if "Flex67" in state else None
		self.Flex68 = state["Flex68"] if "Flex68" in state else None
		self.Flex69 = state["Flex69"] if "Flex69" in state else None
		self.footer2 = state["footer2"] if "footer2" in state else None
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
	def Flex8(self):
		self._getter_access_tracker["Flex8"] = {}
		return self._Flex8
	@Flex8.setter
	def Flex8(self, new_state):
		self._setter_access_tracker["Flex8"] = {}
		self._Flex8 = Flex(new_state)

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
	def Flex11(self):
		self._getter_access_tracker["Flex11"] = {}
		return self._Flex11
	@Flex11.setter
	def Flex11(self, new_state):
		self._setter_access_tracker["Flex11"] = {}
		self._Flex11 = Flex(new_state)

	@property
	def TextBox7(self):
		self._getter_access_tracker["TextBox7"] = {}
		return self._TextBox7
	@TextBox7.setter
	def TextBox7(self, new_state):
		self._setter_access_tracker["TextBox7"] = {}
		self._TextBox7 = TextBox(new_state)

	@property
	def FramerFlex1(self):
		self._getter_access_tracker["FramerFlex1"] = {}
		return self._FramerFlex1
	@FramerFlex1.setter
	def FramerFlex1(self, new_state):
		self._setter_access_tracker["FramerFlex1"] = {}
		self._FramerFlex1 = FramerFlex(new_state)

	@property
	def FramerFlex2(self):
		self._getter_access_tracker["FramerFlex2"] = {}
		return self._FramerFlex2
	@FramerFlex2.setter
	def FramerFlex2(self, new_state):
		self._setter_access_tracker["FramerFlex2"] = {}
		self._FramerFlex2 = FramerFlex(new_state)

	@property
	def TextBox8(self):
		self._getter_access_tracker["TextBox8"] = {}
		return self._TextBox8
	@TextBox8.setter
	def TextBox8(self, new_state):
		self._setter_access_tracker["TextBox8"] = {}
		self._TextBox8 = TextBox(new_state)

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
	def TextBox9(self):
		self._getter_access_tracker["TextBox9"] = {}
		return self._TextBox9
	@TextBox9.setter
	def TextBox9(self, new_state):
		self._setter_access_tracker["TextBox9"] = {}
		self._TextBox9 = TextBox(new_state)

	@property
	def TextBox10(self):
		self._getter_access_tracker["TextBox10"] = {}
		return self._TextBox10
	@TextBox10.setter
	def TextBox10(self, new_state):
		self._setter_access_tracker["TextBox10"] = {}
		self._TextBox10 = TextBox(new_state)

	@property
	def Flex15(self):
		self._getter_access_tracker["Flex15"] = {}
		return self._Flex15
	@Flex15.setter
	def Flex15(self, new_state):
		self._setter_access_tracker["Flex15"] = {}
		self._Flex15 = Flex(new_state)

	@property
	def TextBox11(self):
		self._getter_access_tracker["TextBox11"] = {}
		return self._TextBox11
	@TextBox11.setter
	def TextBox11(self, new_state):
		self._setter_access_tracker["TextBox11"] = {}
		self._TextBox11 = TextBox(new_state)

	@property
	def TextBox12(self):
		self._getter_access_tracker["TextBox12"] = {}
		return self._TextBox12
	@TextBox12.setter
	def TextBox12(self, new_state):
		self._setter_access_tracker["TextBox12"] = {}
		self._TextBox12 = TextBox(new_state)

	@property
	def Flex16(self):
		self._getter_access_tracker["Flex16"] = {}
		return self._Flex16
	@Flex16.setter
	def Flex16(self, new_state):
		self._setter_access_tracker["Flex16"] = {}
		self._Flex16 = Flex(new_state)

	@property
	def Image3(self):
		self._getter_access_tracker["Image3"] = {}
		return self._Image3
	@Image3.setter
	def Image3(self, new_state):
		self._setter_access_tracker["Image3"] = {}
		self._Image3 = Image(new_state)

	@property
	def TextBox13(self):
		self._getter_access_tracker["TextBox13"] = {}
		return self._TextBox13
	@TextBox13.setter
	def TextBox13(self, new_state):
		self._setter_access_tracker["TextBox13"] = {}
		self._TextBox13 = TextBox(new_state)

	@property
	def TextBox14(self):
		self._getter_access_tracker["TextBox14"] = {}
		return self._TextBox14
	@TextBox14.setter
	def TextBox14(self, new_state):
		self._setter_access_tracker["TextBox14"] = {}
		self._TextBox14 = TextBox(new_state)

	@property
	def Image4(self):
		self._getter_access_tracker["Image4"] = {}
		return self._Image4
	@Image4.setter
	def Image4(self, new_state):
		self._setter_access_tracker["Image4"] = {}
		self._Image4 = Image(new_state)

	@property
	def Flex17(self):
		self._getter_access_tracker["Flex17"] = {}
		return self._Flex17
	@Flex17.setter
	def Flex17(self, new_state):
		self._setter_access_tracker["Flex17"] = {}
		self._Flex17 = Flex(new_state)

	@property
	def TextBox15(self):
		self._getter_access_tracker["TextBox15"] = {}
		return self._TextBox15
	@TextBox15.setter
	def TextBox15(self, new_state):
		self._setter_access_tracker["TextBox15"] = {}
		self._TextBox15 = TextBox(new_state)

	@property
	def Image5(self):
		self._getter_access_tracker["Image5"] = {}
		return self._Image5
	@Image5.setter
	def Image5(self, new_state):
		self._setter_access_tracker["Image5"] = {}
		self._Image5 = Image(new_state)

	@property
	def Flex18(self):
		self._getter_access_tracker["Flex18"] = {}
		return self._Flex18
	@Flex18.setter
	def Flex18(self, new_state):
		self._setter_access_tracker["Flex18"] = {}
		self._Flex18 = Flex(new_state)

	@property
	def ShadowFlex3(self):
		self._getter_access_tracker["ShadowFlex3"] = {}
		return self._ShadowFlex3
	@ShadowFlex3.setter
	def ShadowFlex3(self, new_state):
		self._setter_access_tracker["ShadowFlex3"] = {}
		self._ShadowFlex3 = ShadowFlex(new_state)

	@property
	def Flex19(self):
		self._getter_access_tracker["Flex19"] = {}
		return self._Flex19
	@Flex19.setter
	def Flex19(self, new_state):
		self._setter_access_tracker["Flex19"] = {}
		self._Flex19 = Flex(new_state)

	@property
	def TextBox16(self):
		self._getter_access_tracker["TextBox16"] = {}
		return self._TextBox16
	@TextBox16.setter
	def TextBox16(self, new_state):
		self._setter_access_tracker["TextBox16"] = {}
		self._TextBox16 = TextBox(new_state)

	@property
	def Anchor9(self):
		self._getter_access_tracker["Anchor9"] = {}
		return self._Anchor9
	@Anchor9.setter
	def Anchor9(self, new_state):
		self._setter_access_tracker["Anchor9"] = {}
		self._Anchor9 = Anchor(new_state)

	@property
	def TextBox17(self):
		self._getter_access_tracker["TextBox17"] = {}
		return self._TextBox17
	@TextBox17.setter
	def TextBox17(self, new_state):
		self._setter_access_tracker["TextBox17"] = {}
		self._TextBox17 = TextBox(new_state)

	@property
	def ShadowFlex4(self):
		self._getter_access_tracker["ShadowFlex4"] = {}
		return self._ShadowFlex4
	@ShadowFlex4.setter
	def ShadowFlex4(self, new_state):
		self._setter_access_tracker["ShadowFlex4"] = {}
		self._ShadowFlex4 = ShadowFlex(new_state)

	@property
	def TextBox18(self):
		self._getter_access_tracker["TextBox18"] = {}
		return self._TextBox18
	@TextBox18.setter
	def TextBox18(self, new_state):
		self._setter_access_tracker["TextBox18"] = {}
		self._TextBox18 = TextBox(new_state)

	@property
	def TextBox19(self):
		self._getter_access_tracker["TextBox19"] = {}
		return self._TextBox19
	@TextBox19.setter
	def TextBox19(self, new_state):
		self._setter_access_tracker["TextBox19"] = {}
		self._TextBox19 = TextBox(new_state)

	@property
	def Image6(self):
		self._getter_access_tracker["Image6"] = {}
		return self._Image6
	@Image6.setter
	def Image6(self, new_state):
		self._setter_access_tracker["Image6"] = {}
		self._Image6 = Image(new_state)

	@property
	def TextBox20(self):
		self._getter_access_tracker["TextBox20"] = {}
		return self._TextBox20
	@TextBox20.setter
	def TextBox20(self, new_state):
		self._setter_access_tracker["TextBox20"] = {}
		self._TextBox20 = TextBox(new_state)

	@property
	def Image7(self):
		self._getter_access_tracker["Image7"] = {}
		return self._Image7
	@Image7.setter
	def Image7(self, new_state):
		self._setter_access_tracker["Image7"] = {}
		self._Image7 = Image(new_state)

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
	def Image8(self):
		self._getter_access_tracker["Image8"] = {}
		return self._Image8
	@Image8.setter
	def Image8(self, new_state):
		self._setter_access_tracker["Image8"] = {}
		self._Image8 = Image(new_state)

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
	def Anchor10(self):
		self._getter_access_tracker["Anchor10"] = {}
		return self._Anchor10
	@Anchor10.setter
	def Anchor10(self, new_state):
		self._setter_access_tracker["Anchor10"] = {}
		self._Anchor10 = Anchor(new_state)

	@property
	def Flex25(self):
		self._getter_access_tracker["Flex25"] = {}
		return self._Flex25
	@Flex25.setter
	def Flex25(self, new_state):
		self._setter_access_tracker["Flex25"] = {}
		self._Flex25 = Flex(new_state)

	@property
	def Flex26(self):
		self._getter_access_tracker["Flex26"] = {}
		return self._Flex26
	@Flex26.setter
	def Flex26(self, new_state):
		self._setter_access_tracker["Flex26"] = {}
		self._Flex26 = Flex(new_state)

	@property
	def Flex27(self):
		self._getter_access_tracker["Flex27"] = {}
		return self._Flex27
	@Flex27.setter
	def Flex27(self, new_state):
		self._setter_access_tracker["Flex27"] = {}
		self._Flex27 = Flex(new_state)

	@property
	def TextBox25(self):
		self._getter_access_tracker["TextBox25"] = {}
		return self._TextBox25
	@TextBox25.setter
	def TextBox25(self, new_state):
		self._setter_access_tracker["TextBox25"] = {}
		self._TextBox25 = TextBox(new_state)

	@property
	def ShadowFlex5(self):
		self._getter_access_tracker["ShadowFlex5"] = {}
		return self._ShadowFlex5
	@ShadowFlex5.setter
	def ShadowFlex5(self, new_state):
		self._setter_access_tracker["ShadowFlex5"] = {}
		self._ShadowFlex5 = ShadowFlex(new_state)

	@property
	def TextBox26(self):
		self._getter_access_tracker["TextBox26"] = {}
		return self._TextBox26
	@TextBox26.setter
	def TextBox26(self, new_state):
		self._setter_access_tracker["TextBox26"] = {}
		self._TextBox26 = TextBox(new_state)

	@property
	def TextBox27(self):
		self._getter_access_tracker["TextBox27"] = {}
		return self._TextBox27
	@TextBox27.setter
	def TextBox27(self, new_state):
		self._setter_access_tracker["TextBox27"] = {}
		self._TextBox27 = TextBox(new_state)

	@property
	def Image9(self):
		self._getter_access_tracker["Image9"] = {}
		return self._Image9
	@Image9.setter
	def Image9(self, new_state):
		self._setter_access_tracker["Image9"] = {}
		self._Image9 = Image(new_state)

	@property
	def TextBox28(self):
		self._getter_access_tracker["TextBox28"] = {}
		return self._TextBox28
	@TextBox28.setter
	def TextBox28(self, new_state):
		self._setter_access_tracker["TextBox28"] = {}
		self._TextBox28 = TextBox(new_state)

	@property
	def Image10(self):
		self._getter_access_tracker["Image10"] = {}
		return self._Image10
	@Image10.setter
	def Image10(self, new_state):
		self._setter_access_tracker["Image10"] = {}
		self._Image10 = Image(new_state)

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
	def Image11(self):
		self._getter_access_tracker["Image11"] = {}
		return self._Image11
	@Image11.setter
	def Image11(self, new_state):
		self._setter_access_tracker["Image11"] = {}
		self._Image11 = Image(new_state)

	@property
	def Flex28(self):
		self._getter_access_tracker["Flex28"] = {}
		return self._Flex28
	@Flex28.setter
	def Flex28(self, new_state):
		self._setter_access_tracker["Flex28"] = {}
		self._Flex28 = Flex(new_state)

	@property
	def Flex29(self):
		self._getter_access_tracker["Flex29"] = {}
		return self._Flex29
	@Flex29.setter
	def Flex29(self, new_state):
		self._setter_access_tracker["Flex29"] = {}
		self._Flex29 = Flex(new_state)

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
	def Flex30(self):
		self._getter_access_tracker["Flex30"] = {}
		return self._Flex30
	@Flex30.setter
	def Flex30(self, new_state):
		self._setter_access_tracker["Flex30"] = {}
		self._Flex30 = Flex(new_state)

	@property
	def Flex31(self):
		self._getter_access_tracker["Flex31"] = {}
		return self._Flex31
	@Flex31.setter
	def Flex31(self, new_state):
		self._setter_access_tracker["Flex31"] = {}
		self._Flex31 = Flex(new_state)

	@property
	def Flex32(self):
		self._getter_access_tracker["Flex32"] = {}
		return self._Flex32
	@Flex32.setter
	def Flex32(self, new_state):
		self._setter_access_tracker["Flex32"] = {}
		self._Flex32 = Flex(new_state)

	@property
	def Anchor11(self):
		self._getter_access_tracker["Anchor11"] = {}
		return self._Anchor11
	@Anchor11.setter
	def Anchor11(self, new_state):
		self._setter_access_tracker["Anchor11"] = {}
		self._Anchor11 = Anchor(new_state)

	@property
	def Flex33(self):
		self._getter_access_tracker["Flex33"] = {}
		return self._Flex33
	@Flex33.setter
	def Flex33(self, new_state):
		self._setter_access_tracker["Flex33"] = {}
		self._Flex33 = Flex(new_state)

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
	def FramerFlex3(self):
		self._getter_access_tracker["FramerFlex3"] = {}
		return self._FramerFlex3
	@FramerFlex3.setter
	def FramerFlex3(self, new_state):
		self._setter_access_tracker["FramerFlex3"] = {}
		self._FramerFlex3 = FramerFlex(new_state)

	@property
	def FramerFlex4(self):
		self._getter_access_tracker["FramerFlex4"] = {}
		return self._FramerFlex4
	@FramerFlex4.setter
	def FramerFlex4(self, new_state):
		self._setter_access_tracker["FramerFlex4"] = {}
		self._FramerFlex4 = FramerFlex(new_state)

	@property
	def FramerFlex5(self):
		self._getter_access_tracker["FramerFlex5"] = {}
		return self._FramerFlex5
	@FramerFlex5.setter
	def FramerFlex5(self, new_state):
		self._setter_access_tracker["FramerFlex5"] = {}
		self._FramerFlex5 = FramerFlex(new_state)

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
	def TextBox58(self):
		self._getter_access_tracker["TextBox58"] = {}
		return self._TextBox58
	@TextBox58.setter
	def TextBox58(self, new_state):
		self._setter_access_tracker["TextBox58"] = {}
		self._TextBox58 = TextBox(new_state)

	@property
	def TextBox59(self):
		self._getter_access_tracker["TextBox59"] = {}
		return self._TextBox59
	@TextBox59.setter
	def TextBox59(self, new_state):
		self._setter_access_tracker["TextBox59"] = {}
		self._TextBox59 = TextBox(new_state)

	@property
	def TextBox60(self):
		self._getter_access_tracker["TextBox60"] = {}
		return self._TextBox60
	@TextBox60.setter
	def TextBox60(self, new_state):
		self._setter_access_tracker["TextBox60"] = {}
		self._TextBox60 = TextBox(new_state)

	@property
	def TextBox61(self):
		self._getter_access_tracker["TextBox61"] = {}
		return self._TextBox61
	@TextBox61.setter
	def TextBox61(self, new_state):
		self._setter_access_tracker["TextBox61"] = {}
		self._TextBox61 = TextBox(new_state)

	@property
	def ShadowFlex7(self):
		self._getter_access_tracker["ShadowFlex7"] = {}
		return self._ShadowFlex7
	@ShadowFlex7.setter
	def ShadowFlex7(self, new_state):
		self._setter_access_tracker["ShadowFlex7"] = {}
		self._ShadowFlex7 = ShadowFlex(new_state)

	@property
	def ShadowFlex8(self):
		self._getter_access_tracker["ShadowFlex8"] = {}
		return self._ShadowFlex8
	@ShadowFlex8.setter
	def ShadowFlex8(self, new_state):
		self._setter_access_tracker["ShadowFlex8"] = {}
		self._ShadowFlex8 = ShadowFlex(new_state)

	@property
	def NavFlex22(self):
		self._getter_access_tracker["NavFlex22"] = {}
		return self._NavFlex22
	@NavFlex22.setter
	def NavFlex22(self, new_state):
		self._setter_access_tracker["NavFlex22"] = {}
		self._NavFlex22 = NavFlex(new_state)

	@property
	def NavFlex23(self):
		self._getter_access_tracker["NavFlex23"] = {}
		return self._NavFlex23
	@NavFlex23.setter
	def NavFlex23(self, new_state):
		self._setter_access_tracker["NavFlex23"] = {}
		self._NavFlex23 = NavFlex(new_state)

	@property
	def NavFlex24(self):
		self._getter_access_tracker["NavFlex24"] = {}
		return self._NavFlex24
	@NavFlex24.setter
	def NavFlex24(self, new_state):
		self._setter_access_tracker["NavFlex24"] = {}
		self._NavFlex24 = NavFlex(new_state)

	@property
	def NavFlex25(self):
		self._getter_access_tracker["NavFlex25"] = {}
		return self._NavFlex25
	@NavFlex25.setter
	def NavFlex25(self, new_state):
		self._setter_access_tracker["NavFlex25"] = {}
		self._NavFlex25 = NavFlex(new_state)

	@property
	def Image17(self):
		self._getter_access_tracker["Image17"] = {}
		return self._Image17
	@Image17.setter
	def Image17(self, new_state):
		self._setter_access_tracker["Image17"] = {}
		self._Image17 = Image(new_state)

	@property
	def Anchor29(self):
		self._getter_access_tracker["Anchor29"] = {}
		return self._Anchor29
	@Anchor29.setter
	def Anchor29(self, new_state):
		self._setter_access_tracker["Anchor29"] = {}
		self._Anchor29 = Anchor(new_state)

	@property
	def Anchor30(self):
		self._getter_access_tracker["Anchor30"] = {}
		return self._Anchor30
	@Anchor30.setter
	def Anchor30(self, new_state):
		self._setter_access_tracker["Anchor30"] = {}
		self._Anchor30 = Anchor(new_state)

	@property
	def Dropdown2(self):
		self._getter_access_tracker["Dropdown2"] = {}
		return self._Dropdown2
	@Dropdown2.setter
	def Dropdown2(self, new_state):
		self._setter_access_tracker["Dropdown2"] = {}
		self._Dropdown2 = Dropdown(new_state)

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
	def Anchor33(self):
		self._getter_access_tracker["Anchor33"] = {}
		return self._Anchor33
	@Anchor33.setter
	def Anchor33(self, new_state):
		self._setter_access_tracker["Anchor33"] = {}
		self._Anchor33 = Anchor(new_state)

	@property
	def Anchor34(self):
		self._getter_access_tracker["Anchor34"] = {}
		return self._Anchor34
	@Anchor34.setter
	def Anchor34(self, new_state):
		self._setter_access_tracker["Anchor34"] = {}
		self._Anchor34 = Anchor(new_state)

	@property
	def Image18(self):
		self._getter_access_tracker["Image18"] = {}
		return self._Image18
	@Image18.setter
	def Image18(self, new_state):
		self._setter_access_tracker["Image18"] = {}
		self._Image18 = Image(new_state)

	@property
	def Anchor35(self):
		self._getter_access_tracker["Anchor35"] = {}
		return self._Anchor35
	@Anchor35.setter
	def Anchor35(self, new_state):
		self._setter_access_tracker["Anchor35"] = {}
		self._Anchor35 = Anchor(new_state)

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
	def Flex55(self):
		self._getter_access_tracker["Flex55"] = {}
		return self._Flex55
	@Flex55.setter
	def Flex55(self, new_state):
		self._setter_access_tracker["Flex55"] = {}
		self._Flex55 = Flex(new_state)

	@property
	def navbar2(self):
		self._getter_access_tracker["navbar2"] = {}
		return self._navbar2
	@navbar2.setter
	def navbar2(self, new_state):
		self._setter_access_tracker["navbar2"] = {}
		self._navbar2 = Flex(new_state)

	@property
	def Image19(self):
		self._getter_access_tracker["Image19"] = {}
		return self._Image19
	@Image19.setter
	def Image19(self, new_state):
		self._setter_access_tracker["Image19"] = {}
		self._Image19 = Image(new_state)

	@property
	def TextBox62(self):
		self._getter_access_tracker["TextBox62"] = {}
		return self._TextBox62
	@TextBox62.setter
	def TextBox62(self, new_state):
		self._setter_access_tracker["TextBox62"] = {}
		self._TextBox62 = TextBox(new_state)

	@property
	def Image20(self):
		self._getter_access_tracker["Image20"] = {}
		return self._Image20
	@Image20.setter
	def Image20(self, new_state):
		self._setter_access_tracker["Image20"] = {}
		self._Image20 = Image(new_state)

	@property
	def TextBox63(self):
		self._getter_access_tracker["TextBox63"] = {}
		return self._TextBox63
	@TextBox63.setter
	def TextBox63(self, new_state):
		self._setter_access_tracker["TextBox63"] = {}
		self._TextBox63 = TextBox(new_state)

	@property
	def Image21(self):
		self._getter_access_tracker["Image21"] = {}
		return self._Image21
	@Image21.setter
	def Image21(self, new_state):
		self._setter_access_tracker["Image21"] = {}
		self._Image21 = Image(new_state)

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
	def Image22(self):
		self._getter_access_tracker["Image22"] = {}
		return self._Image22
	@Image22.setter
	def Image22(self, new_state):
		self._setter_access_tracker["Image22"] = {}
		self._Image22 = Image(new_state)

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
	def NavFlex26(self):
		self._getter_access_tracker["NavFlex26"] = {}
		return self._NavFlex26
	@NavFlex26.setter
	def NavFlex26(self, new_state):
		self._setter_access_tracker["NavFlex26"] = {}
		self._NavFlex26 = NavFlex(new_state)

	@property
	def NavFlex27(self):
		self._getter_access_tracker["NavFlex27"] = {}
		return self._NavFlex27
	@NavFlex27.setter
	def NavFlex27(self, new_state):
		self._setter_access_tracker["NavFlex27"] = {}
		self._NavFlex27 = NavFlex(new_state)

	@property
	def NavFlex28(self):
		self._getter_access_tracker["NavFlex28"] = {}
		return self._NavFlex28
	@NavFlex28.setter
	def NavFlex28(self, new_state):
		self._setter_access_tracker["NavFlex28"] = {}
		self._NavFlex28 = NavFlex(new_state)

	@property
	def NavFlex29(self):
		self._getter_access_tracker["NavFlex29"] = {}
		return self._NavFlex29
	@NavFlex29.setter
	def NavFlex29(self, new_state):
		self._setter_access_tracker["NavFlex29"] = {}
		self._NavFlex29 = NavFlex(new_state)

	@property
	def Anchor36(self):
		self._getter_access_tracker["Anchor36"] = {}
		return self._Anchor36
	@Anchor36.setter
	def Anchor36(self, new_state):
		self._setter_access_tracker["Anchor36"] = {}
		self._Anchor36 = Anchor(new_state)

	@property
	def Anchor37(self):
		self._getter_access_tracker["Anchor37"] = {}
		return self._Anchor37
	@Anchor37.setter
	def Anchor37(self, new_state):
		self._setter_access_tracker["Anchor37"] = {}
		self._Anchor37 = Anchor(new_state)

	@property
	def Anchor38(self):
		self._getter_access_tracker["Anchor38"] = {}
		return self._Anchor38
	@Anchor38.setter
	def Anchor38(self, new_state):
		self._setter_access_tracker["Anchor38"] = {}
		self._Anchor38 = Anchor(new_state)

	@property
	def Anchor39(self):
		self._getter_access_tracker["Anchor39"] = {}
		return self._Anchor39
	@Anchor39.setter
	def Anchor39(self, new_state):
		self._setter_access_tracker["Anchor39"] = {}
		self._Anchor39 = Anchor(new_state)

	@property
	def Anchor40(self):
		self._getter_access_tracker["Anchor40"] = {}
		return self._Anchor40
	@Anchor40.setter
	def Anchor40(self, new_state):
		self._setter_access_tracker["Anchor40"] = {}
		self._Anchor40 = Anchor(new_state)

	@property
	def Anchor41(self):
		self._getter_access_tracker["Anchor41"] = {}
		return self._Anchor41
	@Anchor41.setter
	def Anchor41(self, new_state):
		self._setter_access_tracker["Anchor41"] = {}
		self._Anchor41 = Anchor(new_state)

	@property
	def Anchor42(self):
		self._getter_access_tracker["Anchor42"] = {}
		return self._Anchor42
	@Anchor42.setter
	def Anchor42(self, new_state):
		self._setter_access_tracker["Anchor42"] = {}
		self._Anchor42 = Anchor(new_state)

	@property
	def TextBox73(self):
		self._getter_access_tracker["TextBox73"] = {}
		return self._TextBox73
	@TextBox73.setter
	def TextBox73(self, new_state):
		self._setter_access_tracker["TextBox73"] = {}
		self._TextBox73 = TextBox(new_state)

	@property
	def TextBox74(self):
		self._getter_access_tracker["TextBox74"] = {}
		return self._TextBox74
	@TextBox74.setter
	def TextBox74(self, new_state):
		self._setter_access_tracker["TextBox74"] = {}
		self._TextBox74 = TextBox(new_state)

	@property
	def TextBox75(self):
		self._getter_access_tracker["TextBox75"] = {}
		return self._TextBox75
	@TextBox75.setter
	def TextBox75(self, new_state):
		self._setter_access_tracker["TextBox75"] = {}
		self._TextBox75 = TextBox(new_state)

	@property
	def TextBox76(self):
		self._getter_access_tracker["TextBox76"] = {}
		return self._TextBox76
	@TextBox76.setter
	def TextBox76(self, new_state):
		self._setter_access_tracker["TextBox76"] = {}
		self._TextBox76 = TextBox(new_state)

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
	def TextBox79(self):
		self._getter_access_tracker["TextBox79"] = {}
		return self._TextBox79
	@TextBox79.setter
	def TextBox79(self, new_state):
		self._setter_access_tracker["TextBox79"] = {}
		self._TextBox79 = TextBox(new_state)

	@property
	def Anchor43(self):
		self._getter_access_tracker["Anchor43"] = {}
		return self._Anchor43
	@Anchor43.setter
	def Anchor43(self, new_state):
		self._setter_access_tracker["Anchor43"] = {}
		self._Anchor43 = Anchor(new_state)

	@property
	def Anchor44(self):
		self._getter_access_tracker["Anchor44"] = {}
		return self._Anchor44
	@Anchor44.setter
	def Anchor44(self, new_state):
		self._setter_access_tracker["Anchor44"] = {}
		self._Anchor44 = Anchor(new_state)

	@property
	def Anchor45(self):
		self._getter_access_tracker["Anchor45"] = {}
		return self._Anchor45
	@Anchor45.setter
	def Anchor45(self, new_state):
		self._setter_access_tracker["Anchor45"] = {}
		self._Anchor45 = Anchor(new_state)

	@property
	def Anchor46(self):
		self._getter_access_tracker["Anchor46"] = {}
		return self._Anchor46
	@Anchor46.setter
	def Anchor46(self, new_state):
		self._setter_access_tracker["Anchor46"] = {}
		self._Anchor46 = Anchor(new_state)

	@property
	def NavFlex30(self):
		self._getter_access_tracker["NavFlex30"] = {}
		return self._NavFlex30
	@NavFlex30.setter
	def NavFlex30(self, new_state):
		self._setter_access_tracker["NavFlex30"] = {}
		self._NavFlex30 = NavFlex(new_state)

	@property
	def NavFlex31(self):
		self._getter_access_tracker["NavFlex31"] = {}
		return self._NavFlex31
	@NavFlex31.setter
	def NavFlex31(self, new_state):
		self._setter_access_tracker["NavFlex31"] = {}
		self._NavFlex31 = NavFlex(new_state)

	@property
	def NavFlex32(self):
		self._getter_access_tracker["NavFlex32"] = {}
		return self._NavFlex32
	@NavFlex32.setter
	def NavFlex32(self, new_state):
		self._setter_access_tracker["NavFlex32"] = {}
		self._NavFlex32 = NavFlex(new_state)

	@property
	def NavFlex33(self):
		self._getter_access_tracker["NavFlex33"] = {}
		return self._NavFlex33
	@NavFlex33.setter
	def NavFlex33(self, new_state):
		self._setter_access_tracker["NavFlex33"] = {}
		self._NavFlex33 = NavFlex(new_state)

	@property
	def NavFlex34(self):
		self._getter_access_tracker["NavFlex34"] = {}
		return self._NavFlex34
	@NavFlex34.setter
	def NavFlex34(self, new_state):
		self._setter_access_tracker["NavFlex34"] = {}
		self._NavFlex34 = NavFlex(new_state)

	@property
	def NavFlex35(self):
		self._getter_access_tracker["NavFlex35"] = {}
		return self._NavFlex35
	@NavFlex35.setter
	def NavFlex35(self, new_state):
		self._setter_access_tracker["NavFlex35"] = {}
		self._NavFlex35 = NavFlex(new_state)

	@property
	def NavFlex36(self):
		self._getter_access_tracker["NavFlex36"] = {}
		return self._NavFlex36
	@NavFlex36.setter
	def NavFlex36(self, new_state):
		self._setter_access_tracker["NavFlex36"] = {}
		self._NavFlex36 = NavFlex(new_state)

	@property
	def ShadowFlex9(self):
		self._getter_access_tracker["ShadowFlex9"] = {}
		return self._ShadowFlex9
	@ShadowFlex9.setter
	def ShadowFlex9(self, new_state):
		self._setter_access_tracker["ShadowFlex9"] = {}
		self._ShadowFlex9 = ShadowFlex(new_state)

	@property
	def Input2(self):
		self._getter_access_tracker["Input2"] = {}
		return self._Input2
	@Input2.setter
	def Input2(self, new_state):
		self._setter_access_tracker["Input2"] = {}
		self._Input2 = Input(new_state)

	@property
	def NavFlex37(self):
		self._getter_access_tracker["NavFlex37"] = {}
		return self._NavFlex37
	@NavFlex37.setter
	def NavFlex37(self, new_state):
		self._setter_access_tracker["NavFlex37"] = {}
		self._NavFlex37 = NavFlex(new_state)

	@property
	def NavFlex38(self):
		self._getter_access_tracker["NavFlex38"] = {}
		return self._NavFlex38
	@NavFlex38.setter
	def NavFlex38(self, new_state):
		self._setter_access_tracker["NavFlex38"] = {}
		self._NavFlex38 = NavFlex(new_state)

	@property
	def NavFlex39(self):
		self._getter_access_tracker["NavFlex39"] = {}
		return self._NavFlex39
	@NavFlex39.setter
	def NavFlex39(self, new_state):
		self._setter_access_tracker["NavFlex39"] = {}
		self._NavFlex39 = NavFlex(new_state)

	@property
	def NavFlex40(self):
		self._getter_access_tracker["NavFlex40"] = {}
		return self._NavFlex40
	@NavFlex40.setter
	def NavFlex40(self, new_state):
		self._setter_access_tracker["NavFlex40"] = {}
		self._NavFlex40 = NavFlex(new_state)

	@property
	def NavFlex41(self):
		self._getter_access_tracker["NavFlex41"] = {}
		return self._NavFlex41
	@NavFlex41.setter
	def NavFlex41(self, new_state):
		self._setter_access_tracker["NavFlex41"] = {}
		self._NavFlex41 = NavFlex(new_state)

	@property
	def NavFlex42(self):
		self._getter_access_tracker["NavFlex42"] = {}
		return self._NavFlex42
	@NavFlex42.setter
	def NavFlex42(self, new_state):
		self._setter_access_tracker["NavFlex42"] = {}
		self._NavFlex42 = NavFlex(new_state)

	@property
	def Flex57(self):
		self._getter_access_tracker["Flex57"] = {}
		return self._Flex57
	@Flex57.setter
	def Flex57(self, new_state):
		self._setter_access_tracker["Flex57"] = {}
		self._Flex57 = Flex(new_state)

	@property
	def TextBox80(self):
		self._getter_access_tracker["TextBox80"] = {}
		return self._TextBox80
	@TextBox80.setter
	def TextBox80(self, new_state):
		self._setter_access_tracker["TextBox80"] = {}
		self._TextBox80 = TextBox(new_state)

	@property
	def Flex58(self):
		self._getter_access_tracker["Flex58"] = {}
		return self._Flex58
	@Flex58.setter
	def Flex58(self, new_state):
		self._setter_access_tracker["Flex58"] = {}
		self._Flex58 = Flex(new_state)

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
	def Flex59(self):
		self._getter_access_tracker["Flex59"] = {}
		return self._Flex59
	@Flex59.setter
	def Flex59(self, new_state):
		self._setter_access_tracker["Flex59"] = {}
		self._Flex59 = Flex(new_state)

	@property
	def Anchor47(self):
		self._getter_access_tracker["Anchor47"] = {}
		return self._Anchor47
	@Anchor47.setter
	def Anchor47(self, new_state):
		self._setter_access_tracker["Anchor47"] = {}
		self._Anchor47 = Anchor(new_state)

	@property
	def Anchor48(self):
		self._getter_access_tracker["Anchor48"] = {}
		return self._Anchor48
	@Anchor48.setter
	def Anchor48(self, new_state):
		self._setter_access_tracker["Anchor48"] = {}
		self._Anchor48 = Anchor(new_state)

	@property
	def Anchor49(self):
		self._getter_access_tracker["Anchor49"] = {}
		return self._Anchor49
	@Anchor49.setter
	def Anchor49(self, new_state):
		self._setter_access_tracker["Anchor49"] = {}
		self._Anchor49 = Anchor(new_state)

	@property
	def Anchor50(self):
		self._getter_access_tracker["Anchor50"] = {}
		return self._Anchor50
	@Anchor50.setter
	def Anchor50(self, new_state):
		self._setter_access_tracker["Anchor50"] = {}
		self._Anchor50 = Anchor(new_state)

	@property
	def Anchor51(self):
		self._getter_access_tracker["Anchor51"] = {}
		return self._Anchor51
	@Anchor51.setter
	def Anchor51(self, new_state):
		self._setter_access_tracker["Anchor51"] = {}
		self._Anchor51 = Anchor(new_state)

	@property
	def Anchor52(self):
		self._getter_access_tracker["Anchor52"] = {}
		return self._Anchor52
	@Anchor52.setter
	def Anchor52(self, new_state):
		self._setter_access_tracker["Anchor52"] = {}
		self._Anchor52 = Anchor(new_state)

	@property
	def Flex60(self):
		self._getter_access_tracker["Flex60"] = {}
		return self._Flex60
	@Flex60.setter
	def Flex60(self, new_state):
		self._setter_access_tracker["Flex60"] = {}
		self._Flex60 = Flex(new_state)

	@property
	def Flex61(self):
		self._getter_access_tracker["Flex61"] = {}
		return self._Flex61
	@Flex61.setter
	def Flex61(self, new_state):
		self._setter_access_tracker["Flex61"] = {}
		self._Flex61 = Flex(new_state)

	@property
	def Flex62(self):
		self._getter_access_tracker["Flex62"] = {}
		return self._Flex62
	@Flex62.setter
	def Flex62(self, new_state):
		self._setter_access_tracker["Flex62"] = {}
		self._Flex62 = Flex(new_state)

	@property
	def TextBox83(self):
		self._getter_access_tracker["TextBox83"] = {}
		return self._TextBox83
	@TextBox83.setter
	def TextBox83(self, new_state):
		self._setter_access_tracker["TextBox83"] = {}
		self._TextBox83 = TextBox(new_state)

	@property
	def Image23(self):
		self._getter_access_tracker["Image23"] = {}
		return self._Image23
	@Image23.setter
	def Image23(self, new_state):
		self._setter_access_tracker["Image23"] = {}
		self._Image23 = Image(new_state)

	@property
	def Flex63(self):
		self._getter_access_tracker["Flex63"] = {}
		return self._Flex63
	@Flex63.setter
	def Flex63(self, new_state):
		self._setter_access_tracker["Flex63"] = {}
		self._Flex63 = Flex(new_state)

	@property
	def Flex64(self):
		self._getter_access_tracker["Flex64"] = {}
		return self._Flex64
	@Flex64.setter
	def Flex64(self, new_state):
		self._setter_access_tracker["Flex64"] = {}
		self._Flex64 = Flex(new_state)

	@property
	def TextBox84(self):
		self._getter_access_tracker["TextBox84"] = {}
		return self._TextBox84
	@TextBox84.setter
	def TextBox84(self, new_state):
		self._setter_access_tracker["TextBox84"] = {}
		self._TextBox84 = TextBox(new_state)

	@property
	def Flex65(self):
		self._getter_access_tracker["Flex65"] = {}
		return self._Flex65
	@Flex65.setter
	def Flex65(self, new_state):
		self._setter_access_tracker["Flex65"] = {}
		self._Flex65 = Flex(new_state)

	@property
	def Flex66(self):
		self._getter_access_tracker["Flex66"] = {}
		return self._Flex66
	@Flex66.setter
	def Flex66(self, new_state):
		self._setter_access_tracker["Flex66"] = {}
		self._Flex66 = Flex(new_state)

	@property
	def Flex67(self):
		self._getter_access_tracker["Flex67"] = {}
		return self._Flex67
	@Flex67.setter
	def Flex67(self, new_state):
		self._setter_access_tracker["Flex67"] = {}
		self._Flex67 = Flex(new_state)

	@property
	def Flex68(self):
		self._getter_access_tracker["Flex68"] = {}
		return self._Flex68
	@Flex68.setter
	def Flex68(self, new_state):
		self._setter_access_tracker["Flex68"] = {}
		self._Flex68 = Flex(new_state)

	@property
	def Flex69(self):
		self._getter_access_tracker["Flex69"] = {}
		return self._Flex69
	@Flex69.setter
	def Flex69(self, new_state):
		self._setter_access_tracker["Flex69"] = {}
		self._Flex69 = Flex(new_state)

	@property
	def footer2(self):
		self._getter_access_tracker["footer2"] = {}
		return self._footer2
	@footer2.setter
	def footer2(self, new_state):
		self._setter_access_tracker["footer2"] = {}
		self._footer2 = Flex(new_state)
  
	def _to_json_fields(self):
		return {
			"Flex8": self._Flex8,
			"Flex9": self._Flex9,
			"Flex10": self._Flex10,
			"Flex11": self._Flex11,
			"TextBox7": self._TextBox7,
			"FramerFlex1": self._FramerFlex1,
			"FramerFlex2": self._FramerFlex2,
			"TextBox8": self._TextBox8,
			"Flex12": self._Flex12,
			"Flex13": self._Flex13,
			"Flex14": self._Flex14,
			"TextBox9": self._TextBox9,
			"TextBox10": self._TextBox10,
			"Flex15": self._Flex15,
			"TextBox11": self._TextBox11,
			"TextBox12": self._TextBox12,
			"Flex16": self._Flex16,
			"Image3": self._Image3,
			"TextBox13": self._TextBox13,
			"TextBox14": self._TextBox14,
			"Image4": self._Image4,
			"Flex17": self._Flex17,
			"TextBox15": self._TextBox15,
			"Image5": self._Image5,
			"Flex18": self._Flex18,
			"ShadowFlex3": self._ShadowFlex3,
			"Flex19": self._Flex19,
			"TextBox16": self._TextBox16,
			"Anchor9": self._Anchor9,
			"TextBox17": self._TextBox17,
			"ShadowFlex4": self._ShadowFlex4,
			"TextBox18": self._TextBox18,
			"TextBox19": self._TextBox19,
			"Image6": self._Image6,
			"TextBox20": self._TextBox20,
			"Image7": self._Image7,
			"TextBox21": self._TextBox21,
			"TextBox22": self._TextBox22,
			"Image8": self._Image8,
			"Flex20": self._Flex20,
			"Flex21": self._Flex21,
			"TextBox23": self._TextBox23,
			"TextBox24": self._TextBox24,
			"Flex22": self._Flex22,
			"Flex23": self._Flex23,
			"Flex24": self._Flex24,
			"Anchor10": self._Anchor10,
			"Flex25": self._Flex25,
			"Flex26": self._Flex26,
			"Flex27": self._Flex27,
			"TextBox25": self._TextBox25,
			"ShadowFlex5": self._ShadowFlex5,
			"TextBox26": self._TextBox26,
			"TextBox27": self._TextBox27,
			"Image9": self._Image9,
			"TextBox28": self._TextBox28,
			"Image10": self._Image10,
			"TextBox29": self._TextBox29,
			"TextBox30": self._TextBox30,
			"Image11": self._Image11,
			"Flex28": self._Flex28,
			"Flex29": self._Flex29,
			"TextBox31": self._TextBox31,
			"TextBox32": self._TextBox32,
			"Flex30": self._Flex30,
			"Flex31": self._Flex31,
			"Flex32": self._Flex32,
			"Anchor11": self._Anchor11,
			"Flex33": self._Flex33,
			"Flex34": self._Flex34,
			"Flex35": self._Flex35,
			"FramerFlex3": self._FramerFlex3,
			"FramerFlex4": self._FramerFlex4,
			"FramerFlex5": self._FramerFlex5,
			"TextBox56": self._TextBox56,
			"TextBox57": self._TextBox57,
			"TextBox58": self._TextBox58,
			"TextBox59": self._TextBox59,
			"TextBox60": self._TextBox60,
			"TextBox61": self._TextBox61,
			"ShadowFlex7": self._ShadowFlex7,
			"ShadowFlex8": self._ShadowFlex8,
			"NavFlex22": self._NavFlex22,
			"NavFlex23": self._NavFlex23,
			"NavFlex24": self._NavFlex24,
			"NavFlex25": self._NavFlex25,
			"Image17": self._Image17,
			"Anchor29": self._Anchor29,
			"Anchor30": self._Anchor30,
			"Dropdown2": self._Dropdown2,
			"Anchor31": self._Anchor31,
			"Anchor32": self._Anchor32,
			"Anchor33": self._Anchor33,
			"Anchor34": self._Anchor34,
			"Image18": self._Image18,
			"Anchor35": self._Anchor35,
			"Flex50": self._Flex50,
			"Flex51": self._Flex51,
			"Flex52": self._Flex52,
			"Flex53": self._Flex53,
			"Flex54": self._Flex54,
			"Flex55": self._Flex55,
			"navbar2": self._navbar2,
			"Image19": self._Image19,
			"TextBox62": self._TextBox62,
			"Image20": self._Image20,
			"TextBox63": self._TextBox63,
			"Image21": self._Image21,
			"TextBox64": self._TextBox64,
			"TextBox65": self._TextBox65,
			"Image22": self._Image22,
			"TextBox66": self._TextBox66,
			"TextBox67": self._TextBox67,
			"TextBox68": self._TextBox68,
			"TextBox69": self._TextBox69,
			"TextBox70": self._TextBox70,
			"TextBox71": self._TextBox71,
			"TextBox72": self._TextBox72,
			"NavFlex26": self._NavFlex26,
			"NavFlex27": self._NavFlex27,
			"NavFlex28": self._NavFlex28,
			"NavFlex29": self._NavFlex29,
			"Anchor36": self._Anchor36,
			"Anchor37": self._Anchor37,
			"Anchor38": self._Anchor38,
			"Anchor39": self._Anchor39,
			"Anchor40": self._Anchor40,
			"Anchor41": self._Anchor41,
			"Anchor42": self._Anchor42,
			"TextBox73": self._TextBox73,
			"TextBox74": self._TextBox74,
			"TextBox75": self._TextBox75,
			"TextBox76": self._TextBox76,
			"TextBox77": self._TextBox77,
			"TextBox78": self._TextBox78,
			"TextBox79": self._TextBox79,
			"Anchor43": self._Anchor43,
			"Anchor44": self._Anchor44,
			"Anchor45": self._Anchor45,
			"Anchor46": self._Anchor46,
			"NavFlex30": self._NavFlex30,
			"NavFlex31": self._NavFlex31,
			"NavFlex32": self._NavFlex32,
			"NavFlex33": self._NavFlex33,
			"NavFlex34": self._NavFlex34,
			"NavFlex35": self._NavFlex35,
			"NavFlex36": self._NavFlex36,
			"ShadowFlex9": self._ShadowFlex9,
			"Input2": self._Input2,
			"NavFlex37": self._NavFlex37,
			"NavFlex38": self._NavFlex38,
			"NavFlex39": self._NavFlex39,
			"NavFlex40": self._NavFlex40,
			"NavFlex41": self._NavFlex41,
			"NavFlex42": self._NavFlex42,
			"Flex57": self._Flex57,
			"TextBox80": self._TextBox80,
			"Flex58": self._Flex58,
			"TextBox81": self._TextBox81,
			"TextBox82": self._TextBox82,
			"Flex59": self._Flex59,
			"Anchor47": self._Anchor47,
			"Anchor48": self._Anchor48,
			"Anchor49": self._Anchor49,
			"Anchor50": self._Anchor50,
			"Anchor51": self._Anchor51,
			"Anchor52": self._Anchor52,
			"Flex60": self._Flex60,
			"Flex61": self._Flex61,
			"Flex62": self._Flex62,
			"TextBox83": self._TextBox83,
			"Image23": self._Image23,
			"Flex63": self._Flex63,
			"Flex64": self._Flex64,
			"TextBox84": self._TextBox84,
			"Flex65": self._Flex65,
			"Flex66": self._Flex66,
			"Flex67": self._Flex67,
			"Flex68": self._Flex68,
			"Flex69": self._Flex69,
			"footer2": self._footer2
			}
  