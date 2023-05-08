from typing import Union, Any
from atri_react.TextBox import TextBox
from manifests.ShadowFlex import ShadowFlex
from manifests.NavFlex import NavFlex
from atri_react.Image import Image
from atri_react.Anchor import Anchor
from atri_react.Dropdown import Dropdown
from atri_react.Flex import Flex
from atri_react.Input import Input
from atri_react.Textarea import Textarea
from atri_react.Checkbox import Checkbox
from manifests.FramerFlex import FramerFlex


  
class Page:
	def __init__(self, state: Union[Any, None]):
		self.event_data = None
		self.event_alias = None
		self._setter_access_tracker = {}
		self.TextBox1 = state["TextBox1"] if "TextBox1" in state else None
		self.TextBox2 = state["TextBox2"] if "TextBox2" in state else None
		self.TextBox3 = state["TextBox3"] if "TextBox3" in state else None
		self.TextBox4 = state["TextBox4"] if "TextBox4" in state else None
		self.TextBox5 = state["TextBox5"] if "TextBox5" in state else None
		self.TextBox6 = state["TextBox6"] if "TextBox6" in state else None
		self.ShadowFlex1 = state["ShadowFlex1"] if "ShadowFlex1" in state else None
		self.ShadowFlex2 = state["ShadowFlex2"] if "ShadowFlex2" in state else None
		self.NavFlex1 = state["NavFlex1"] if "NavFlex1" in state else None
		self.NavFlex2 = state["NavFlex2"] if "NavFlex2" in state else None
		self.NavFlex3 = state["NavFlex3"] if "NavFlex3" in state else None
		self.NavFlex4 = state["NavFlex4"] if "NavFlex4" in state else None
		self.Image1 = state["Image1"] if "Image1" in state else None
		self.Anchor1 = state["Anchor1"] if "Anchor1" in state else None
		self.Anchor2 = state["Anchor2"] if "Anchor2" in state else None
		self.Dropdown1 = state["Dropdown1"] if "Dropdown1" in state else None
		self.Anchor3 = state["Anchor3"] if "Anchor3" in state else None
		self.Anchor4 = state["Anchor4"] if "Anchor4" in state else None
		self.Anchor5 = state["Anchor5"] if "Anchor5" in state else None
		self.Anchor6 = state["Anchor6"] if "Anchor6" in state else None
		self.Image2 = state["Image2"] if "Image2" in state else None
		self.Anchor7 = state["Anchor7"] if "Anchor7" in state else None
		self.Flex1 = state["Flex1"] if "Flex1" in state else None
		self.Flex2 = state["Flex2"] if "Flex2" in state else None
		self.Flex3 = state["Flex3"] if "Flex3" in state else None
		self.Flex4 = state["Flex4"] if "Flex4" in state else None
		self.Flex5 = state["Flex5"] if "Flex5" in state else None
		self.Flex6 = state["Flex6"] if "Flex6" in state else None
		self.navbar1 = state["navbar1"] if "navbar1" in state else None
		self.Flex8 = state["Flex8"] if "Flex8" in state else None
		self.Flex9 = state["Flex9"] if "Flex9" in state else None
		self.Flex10 = state["Flex10"] if "Flex10" in state else None
		self.Flex11 = state["Flex11"] if "Flex11" in state else None
		self.Flex12 = state["Flex12"] if "Flex12" in state else None
		self.Flex13 = state["Flex13"] if "Flex13" in state else None
		self.TextBox7 = state["TextBox7"] if "TextBox7" in state else None
		self.TextBox8 = state["TextBox8"] if "TextBox8" in state else None
		self.Flex14 = state["Flex14"] if "Flex14" in state else None
		self.Flex15 = state["Flex15"] if "Flex15" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
		self.Image4 = state["Image4"] if "Image4" in state else None
		self.TextBox9 = state["TextBox9"] if "TextBox9" in state else None
		self.TextBox10 = state["TextBox10"] if "TextBox10" in state else None
		self.Anchor8 = state["Anchor8"] if "Anchor8" in state else None
		self.Flex16 = state["Flex16"] if "Flex16" in state else None
		self.TextBox11 = state["TextBox11"] if "TextBox11" in state else None
		self.Input1 = state["Input1"] if "Input1" in state else None
		self.Input2 = state["Input2"] if "Input2" in state else None
		self.TextBox12 = state["TextBox12"] if "TextBox12" in state else None
		self.Flex17 = state["Flex17"] if "Flex17" in state else None
		self.Flex18 = state["Flex18"] if "Flex18" in state else None
		self.TextBox13 = state["TextBox13"] if "TextBox13" in state else None
		self.Textarea1 = state["Textarea1"] if "Textarea1" in state else None
		self.Flex19 = state["Flex19"] if "Flex19" in state else None
		self.Checkbox1 = state["Checkbox1"] if "Checkbox1" in state else None
		self.Flex20 = state["Flex20"] if "Flex20" in state else None
		self.ShadowFlex3 = state["ShadowFlex3"] if "ShadowFlex3" in state else None
		self.TextBox14 = state["TextBox14"] if "TextBox14" in state else None
		self.FramerFlex1 = state["FramerFlex1"] if "FramerFlex1" in state else None
		self.FramerFlex2 = state["FramerFlex2"] if "FramerFlex2" in state else None
		self.FramerFlex3 = state["FramerFlex3"] if "FramerFlex3" in state else None
		self.FramerFlex4 = state["FramerFlex4"] if "FramerFlex4" in state else None
		self.Image5 = state["Image5"] if "Image5" in state else None
		self.TextBox15 = state["TextBox15"] if "TextBox15" in state else None
		self.Image6 = state["Image6"] if "Image6" in state else None
		self.TextBox16 = state["TextBox16"] if "TextBox16" in state else None
		self.Image7 = state["Image7"] if "Image7" in state else None
		self.TextBox17 = state["TextBox17"] if "TextBox17" in state else None
		self.TextBox18 = state["TextBox18"] if "TextBox18" in state else None
		self.Image8 = state["Image8"] if "Image8" in state else None
		self.TextBox19 = state["TextBox19"] if "TextBox19" in state else None
		self.TextBox20 = state["TextBox20"] if "TextBox20" in state else None
		self.TextBox21 = state["TextBox21"] if "TextBox21" in state else None
		self.TextBox22 = state["TextBox22"] if "TextBox22" in state else None
		self.TextBox23 = state["TextBox23"] if "TextBox23" in state else None
		self.TextBox24 = state["TextBox24"] if "TextBox24" in state else None
		self.TextBox25 = state["TextBox25"] if "TextBox25" in state else None
		self.NavFlex5 = state["NavFlex5"] if "NavFlex5" in state else None
		self.NavFlex6 = state["NavFlex6"] if "NavFlex6" in state else None
		self.NavFlex7 = state["NavFlex7"] if "NavFlex7" in state else None
		self.NavFlex8 = state["NavFlex8"] if "NavFlex8" in state else None
		self.Anchor9 = state["Anchor9"] if "Anchor9" in state else None
		self.Anchor10 = state["Anchor10"] if "Anchor10" in state else None
		self.Anchor11 = state["Anchor11"] if "Anchor11" in state else None
		self.Anchor12 = state["Anchor12"] if "Anchor12" in state else None
		self.Anchor13 = state["Anchor13"] if "Anchor13" in state else None
		self.Anchor14 = state["Anchor14"] if "Anchor14" in state else None
		self.Anchor15 = state["Anchor15"] if "Anchor15" in state else None
		self.TextBox26 = state["TextBox26"] if "TextBox26" in state else None
		self.TextBox27 = state["TextBox27"] if "TextBox27" in state else None
		self.TextBox28 = state["TextBox28"] if "TextBox28" in state else None
		self.TextBox29 = state["TextBox29"] if "TextBox29" in state else None
		self.TextBox30 = state["TextBox30"] if "TextBox30" in state else None
		self.TextBox31 = state["TextBox31"] if "TextBox31" in state else None
		self.TextBox32 = state["TextBox32"] if "TextBox32" in state else None
		self.Anchor16 = state["Anchor16"] if "Anchor16" in state else None
		self.Anchor17 = state["Anchor17"] if "Anchor17" in state else None
		self.Anchor18 = state["Anchor18"] if "Anchor18" in state else None
		self.Anchor19 = state["Anchor19"] if "Anchor19" in state else None
		self.NavFlex9 = state["NavFlex9"] if "NavFlex9" in state else None
		self.NavFlex10 = state["NavFlex10"] if "NavFlex10" in state else None
		self.NavFlex11 = state["NavFlex11"] if "NavFlex11" in state else None
		self.NavFlex12 = state["NavFlex12"] if "NavFlex12" in state else None
		self.NavFlex13 = state["NavFlex13"] if "NavFlex13" in state else None
		self.NavFlex14 = state["NavFlex14"] if "NavFlex14" in state else None
		self.NavFlex15 = state["NavFlex15"] if "NavFlex15" in state else None
		self.ShadowFlex4 = state["ShadowFlex4"] if "ShadowFlex4" in state else None
		self.Input3 = state["Input3"] if "Input3" in state else None
		self.NavFlex16 = state["NavFlex16"] if "NavFlex16" in state else None
		self.NavFlex17 = state["NavFlex17"] if "NavFlex17" in state else None
		self.NavFlex18 = state["NavFlex18"] if "NavFlex18" in state else None
		self.NavFlex19 = state["NavFlex19"] if "NavFlex19" in state else None
		self.NavFlex20 = state["NavFlex20"] if "NavFlex20" in state else None
		self.NavFlex21 = state["NavFlex21"] if "NavFlex21" in state else None
		self.Flex22 = state["Flex22"] if "Flex22" in state else None
		self.TextBox33 = state["TextBox33"] if "TextBox33" in state else None
		self.Flex23 = state["Flex23"] if "Flex23" in state else None
		self.TextBox34 = state["TextBox34"] if "TextBox34" in state else None
		self.TextBox35 = state["TextBox35"] if "TextBox35" in state else None
		self.Flex24 = state["Flex24"] if "Flex24" in state else None
		self.Anchor20 = state["Anchor20"] if "Anchor20" in state else None
		self.Anchor21 = state["Anchor21"] if "Anchor21" in state else None
		self.Anchor22 = state["Anchor22"] if "Anchor22" in state else None
		self.Anchor23 = state["Anchor23"] if "Anchor23" in state else None
		self.Anchor24 = state["Anchor24"] if "Anchor24" in state else None
		self.Anchor25 = state["Anchor25"] if "Anchor25" in state else None
		self.Flex25 = state["Flex25"] if "Flex25" in state else None
		self.Flex26 = state["Flex26"] if "Flex26" in state else None
		self.Flex27 = state["Flex27"] if "Flex27" in state else None
		self.TextBox36 = state["TextBox36"] if "TextBox36" in state else None
		self.Image9 = state["Image9"] if "Image9" in state else None
		self.Flex28 = state["Flex28"] if "Flex28" in state else None
		self.Flex29 = state["Flex29"] if "Flex29" in state else None
		self.TextBox37 = state["TextBox37"] if "TextBox37" in state else None
		self.Flex30 = state["Flex30"] if "Flex30" in state else None
		self.Flex31 = state["Flex31"] if "Flex31" in state else None
		self.Flex32 = state["Flex32"] if "Flex32" in state else None
		self.Flex33 = state["Flex33"] if "Flex33" in state else None
		self.Flex34 = state["Flex34"] if "Flex34" in state else None
		self.footer1 = state["footer1"] if "footer1" in state else None
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
	def TextBox1(self):
		self._getter_access_tracker["TextBox1"] = {}
		return self._TextBox1
	@TextBox1.setter
	def TextBox1(self, new_state):
		self._setter_access_tracker["TextBox1"] = {}
		self._TextBox1 = TextBox(new_state)

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
	def TextBox4(self):
		self._getter_access_tracker["TextBox4"] = {}
		return self._TextBox4
	@TextBox4.setter
	def TextBox4(self, new_state):
		self._setter_access_tracker["TextBox4"] = {}
		self._TextBox4 = TextBox(new_state)

	@property
	def TextBox5(self):
		self._getter_access_tracker["TextBox5"] = {}
		return self._TextBox5
	@TextBox5.setter
	def TextBox5(self, new_state):
		self._setter_access_tracker["TextBox5"] = {}
		self._TextBox5 = TextBox(new_state)

	@property
	def TextBox6(self):
		self._getter_access_tracker["TextBox6"] = {}
		return self._TextBox6
	@TextBox6.setter
	def TextBox6(self, new_state):
		self._setter_access_tracker["TextBox6"] = {}
		self._TextBox6 = TextBox(new_state)

	@property
	def ShadowFlex1(self):
		self._getter_access_tracker["ShadowFlex1"] = {}
		return self._ShadowFlex1
	@ShadowFlex1.setter
	def ShadowFlex1(self, new_state):
		self._setter_access_tracker["ShadowFlex1"] = {}
		self._ShadowFlex1 = ShadowFlex(new_state)

	@property
	def ShadowFlex2(self):
		self._getter_access_tracker["ShadowFlex2"] = {}
		return self._ShadowFlex2
	@ShadowFlex2.setter
	def ShadowFlex2(self, new_state):
		self._setter_access_tracker["ShadowFlex2"] = {}
		self._ShadowFlex2 = ShadowFlex(new_state)

	@property
	def NavFlex1(self):
		self._getter_access_tracker["NavFlex1"] = {}
		return self._NavFlex1
	@NavFlex1.setter
	def NavFlex1(self, new_state):
		self._setter_access_tracker["NavFlex1"] = {}
		self._NavFlex1 = NavFlex(new_state)

	@property
	def NavFlex2(self):
		self._getter_access_tracker["NavFlex2"] = {}
		return self._NavFlex2
	@NavFlex2.setter
	def NavFlex2(self, new_state):
		self._setter_access_tracker["NavFlex2"] = {}
		self._NavFlex2 = NavFlex(new_state)

	@property
	def NavFlex3(self):
		self._getter_access_tracker["NavFlex3"] = {}
		return self._NavFlex3
	@NavFlex3.setter
	def NavFlex3(self, new_state):
		self._setter_access_tracker["NavFlex3"] = {}
		self._NavFlex3 = NavFlex(new_state)

	@property
	def NavFlex4(self):
		self._getter_access_tracker["NavFlex4"] = {}
		return self._NavFlex4
	@NavFlex4.setter
	def NavFlex4(self, new_state):
		self._setter_access_tracker["NavFlex4"] = {}
		self._NavFlex4 = NavFlex(new_state)

	@property
	def Image1(self):
		self._getter_access_tracker["Image1"] = {}
		return self._Image1
	@Image1.setter
	def Image1(self, new_state):
		self._setter_access_tracker["Image1"] = {}
		self._Image1 = Image(new_state)

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
	def Dropdown1(self):
		self._getter_access_tracker["Dropdown1"] = {}
		return self._Dropdown1
	@Dropdown1.setter
	def Dropdown1(self, new_state):
		self._setter_access_tracker["Dropdown1"] = {}
		self._Dropdown1 = Dropdown(new_state)

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
	def Anchor5(self):
		self._getter_access_tracker["Anchor5"] = {}
		return self._Anchor5
	@Anchor5.setter
	def Anchor5(self, new_state):
		self._setter_access_tracker["Anchor5"] = {}
		self._Anchor5 = Anchor(new_state)

	@property
	def Anchor6(self):
		self._getter_access_tracker["Anchor6"] = {}
		return self._Anchor6
	@Anchor6.setter
	def Anchor6(self, new_state):
		self._setter_access_tracker["Anchor6"] = {}
		self._Anchor6 = Anchor(new_state)

	@property
	def Image2(self):
		self._getter_access_tracker["Image2"] = {}
		return self._Image2
	@Image2.setter
	def Image2(self, new_state):
		self._setter_access_tracker["Image2"] = {}
		self._Image2 = Image(new_state)

	@property
	def Anchor7(self):
		self._getter_access_tracker["Anchor7"] = {}
		return self._Anchor7
	@Anchor7.setter
	def Anchor7(self, new_state):
		self._setter_access_tracker["Anchor7"] = {}
		self._Anchor7 = Anchor(new_state)

	@property
	def Flex1(self):
		self._getter_access_tracker["Flex1"] = {}
		return self._Flex1
	@Flex1.setter
	def Flex1(self, new_state):
		self._setter_access_tracker["Flex1"] = {}
		self._Flex1 = Flex(new_state)

	@property
	def Flex2(self):
		self._getter_access_tracker["Flex2"] = {}
		return self._Flex2
	@Flex2.setter
	def Flex2(self, new_state):
		self._setter_access_tracker["Flex2"] = {}
		self._Flex2 = Flex(new_state)

	@property
	def Flex3(self):
		self._getter_access_tracker["Flex3"] = {}
		return self._Flex3
	@Flex3.setter
	def Flex3(self, new_state):
		self._setter_access_tracker["Flex3"] = {}
		self._Flex3 = Flex(new_state)

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
	def navbar1(self):
		self._getter_access_tracker["navbar1"] = {}
		return self._navbar1
	@navbar1.setter
	def navbar1(self, new_state):
		self._setter_access_tracker["navbar1"] = {}
		self._navbar1 = Flex(new_state)

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
	def TextBox7(self):
		self._getter_access_tracker["TextBox7"] = {}
		return self._TextBox7
	@TextBox7.setter
	def TextBox7(self, new_state):
		self._setter_access_tracker["TextBox7"] = {}
		self._TextBox7 = TextBox(new_state)

	@property
	def TextBox8(self):
		self._getter_access_tracker["TextBox8"] = {}
		return self._TextBox8
	@TextBox8.setter
	def TextBox8(self, new_state):
		self._setter_access_tracker["TextBox8"] = {}
		self._TextBox8 = TextBox(new_state)

	@property
	def Flex14(self):
		self._getter_access_tracker["Flex14"] = {}
		return self._Flex14
	@Flex14.setter
	def Flex14(self, new_state):
		self._setter_access_tracker["Flex14"] = {}
		self._Flex14 = Flex(new_state)

	@property
	def Flex15(self):
		self._getter_access_tracker["Flex15"] = {}
		return self._Flex15
	@Flex15.setter
	def Flex15(self, new_state):
		self._setter_access_tracker["Flex15"] = {}
		self._Flex15 = Flex(new_state)

	@property
	def Image3(self):
		self._getter_access_tracker["Image3"] = {}
		return self._Image3
	@Image3.setter
	def Image3(self, new_state):
		self._setter_access_tracker["Image3"] = {}
		self._Image3 = Image(new_state)

	@property
	def Image4(self):
		self._getter_access_tracker["Image4"] = {}
		return self._Image4
	@Image4.setter
	def Image4(self, new_state):
		self._setter_access_tracker["Image4"] = {}
		self._Image4 = Image(new_state)

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
	def Anchor8(self):
		self._getter_access_tracker["Anchor8"] = {}
		return self._Anchor8
	@Anchor8.setter
	def Anchor8(self, new_state):
		self._setter_access_tracker["Anchor8"] = {}
		self._Anchor8 = Anchor(new_state)

	@property
	def Flex16(self):
		self._getter_access_tracker["Flex16"] = {}
		return self._Flex16
	@Flex16.setter
	def Flex16(self, new_state):
		self._setter_access_tracker["Flex16"] = {}
		self._Flex16 = Flex(new_state)

	@property
	def TextBox11(self):
		self._getter_access_tracker["TextBox11"] = {}
		return self._TextBox11
	@TextBox11.setter
	def TextBox11(self, new_state):
		self._setter_access_tracker["TextBox11"] = {}
		self._TextBox11 = TextBox(new_state)

	@property
	def Input1(self):
		self._getter_access_tracker["Input1"] = {}
		return self._Input1
	@Input1.setter
	def Input1(self, new_state):
		self._setter_access_tracker["Input1"] = {}
		self._Input1 = Input(new_state)

	@property
	def Input2(self):
		self._getter_access_tracker["Input2"] = {}
		return self._Input2
	@Input2.setter
	def Input2(self, new_state):
		self._setter_access_tracker["Input2"] = {}
		self._Input2 = Input(new_state)

	@property
	def TextBox12(self):
		self._getter_access_tracker["TextBox12"] = {}
		return self._TextBox12
	@TextBox12.setter
	def TextBox12(self, new_state):
		self._setter_access_tracker["TextBox12"] = {}
		self._TextBox12 = TextBox(new_state)

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
	def TextBox13(self):
		self._getter_access_tracker["TextBox13"] = {}
		return self._TextBox13
	@TextBox13.setter
	def TextBox13(self, new_state):
		self._setter_access_tracker["TextBox13"] = {}
		self._TextBox13 = TextBox(new_state)

	@property
	def Textarea1(self):
		self._getter_access_tracker["Textarea1"] = {}
		return self._Textarea1
	@Textarea1.setter
	def Textarea1(self, new_state):
		self._setter_access_tracker["Textarea1"] = {}
		self._Textarea1 = Textarea(new_state)

	@property
	def Flex19(self):
		self._getter_access_tracker["Flex19"] = {}
		return self._Flex19
	@Flex19.setter
	def Flex19(self, new_state):
		self._setter_access_tracker["Flex19"] = {}
		self._Flex19 = Flex(new_state)

	@property
	def Checkbox1(self):
		self._getter_access_tracker["Checkbox1"] = {}
		return self._Checkbox1
	@Checkbox1.setter
	def Checkbox1(self, new_state):
		self._setter_access_tracker["Checkbox1"] = {}
		self._Checkbox1 = Checkbox(new_state)

	@property
	def Flex20(self):
		self._getter_access_tracker["Flex20"] = {}
		return self._Flex20
	@Flex20.setter
	def Flex20(self, new_state):
		self._setter_access_tracker["Flex20"] = {}
		self._Flex20 = Flex(new_state)

	@property
	def ShadowFlex3(self):
		self._getter_access_tracker["ShadowFlex3"] = {}
		return self._ShadowFlex3
	@ShadowFlex3.setter
	def ShadowFlex3(self, new_state):
		self._setter_access_tracker["ShadowFlex3"] = {}
		self._ShadowFlex3 = ShadowFlex(new_state)

	@property
	def TextBox14(self):
		self._getter_access_tracker["TextBox14"] = {}
		return self._TextBox14
	@TextBox14.setter
	def TextBox14(self, new_state):
		self._setter_access_tracker["TextBox14"] = {}
		self._TextBox14 = TextBox(new_state)

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
	def Image5(self):
		self._getter_access_tracker["Image5"] = {}
		return self._Image5
	@Image5.setter
	def Image5(self, new_state):
		self._setter_access_tracker["Image5"] = {}
		self._Image5 = Image(new_state)

	@property
	def TextBox15(self):
		self._getter_access_tracker["TextBox15"] = {}
		return self._TextBox15
	@TextBox15.setter
	def TextBox15(self, new_state):
		self._setter_access_tracker["TextBox15"] = {}
		self._TextBox15 = TextBox(new_state)

	@property
	def Image6(self):
		self._getter_access_tracker["Image6"] = {}
		return self._Image6
	@Image6.setter
	def Image6(self, new_state):
		self._setter_access_tracker["Image6"] = {}
		self._Image6 = Image(new_state)

	@property
	def TextBox16(self):
		self._getter_access_tracker["TextBox16"] = {}
		return self._TextBox16
	@TextBox16.setter
	def TextBox16(self, new_state):
		self._setter_access_tracker["TextBox16"] = {}
		self._TextBox16 = TextBox(new_state)

	@property
	def Image7(self):
		self._getter_access_tracker["Image7"] = {}
		return self._Image7
	@Image7.setter
	def Image7(self, new_state):
		self._setter_access_tracker["Image7"] = {}
		self._Image7 = Image(new_state)

	@property
	def TextBox17(self):
		self._getter_access_tracker["TextBox17"] = {}
		return self._TextBox17
	@TextBox17.setter
	def TextBox17(self, new_state):
		self._setter_access_tracker["TextBox17"] = {}
		self._TextBox17 = TextBox(new_state)

	@property
	def TextBox18(self):
		self._getter_access_tracker["TextBox18"] = {}
		return self._TextBox18
	@TextBox18.setter
	def TextBox18(self, new_state):
		self._setter_access_tracker["TextBox18"] = {}
		self._TextBox18 = TextBox(new_state)

	@property
	def Image8(self):
		self._getter_access_tracker["Image8"] = {}
		return self._Image8
	@Image8.setter
	def Image8(self, new_state):
		self._setter_access_tracker["Image8"] = {}
		self._Image8 = Image(new_state)

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
	def Anchor9(self):
		self._getter_access_tracker["Anchor9"] = {}
		return self._Anchor9
	@Anchor9.setter
	def Anchor9(self, new_state):
		self._setter_access_tracker["Anchor9"] = {}
		self._Anchor9 = Anchor(new_state)

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
	def TextBox28(self):
		self._getter_access_tracker["TextBox28"] = {}
		return self._TextBox28
	@TextBox28.setter
	def TextBox28(self, new_state):
		self._setter_access_tracker["TextBox28"] = {}
		self._TextBox28 = TextBox(new_state)

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
	def NavFlex13(self):
		self._getter_access_tracker["NavFlex13"] = {}
		return self._NavFlex13
	@NavFlex13.setter
	def NavFlex13(self, new_state):
		self._setter_access_tracker["NavFlex13"] = {}
		self._NavFlex13 = NavFlex(new_state)

	@property
	def NavFlex14(self):
		self._getter_access_tracker["NavFlex14"] = {}
		return self._NavFlex14
	@NavFlex14.setter
	def NavFlex14(self, new_state):
		self._setter_access_tracker["NavFlex14"] = {}
		self._NavFlex14 = NavFlex(new_state)

	@property
	def NavFlex15(self):
		self._getter_access_tracker["NavFlex15"] = {}
		return self._NavFlex15
	@NavFlex15.setter
	def NavFlex15(self, new_state):
		self._setter_access_tracker["NavFlex15"] = {}
		self._NavFlex15 = NavFlex(new_state)

	@property
	def ShadowFlex4(self):
		self._getter_access_tracker["ShadowFlex4"] = {}
		return self._ShadowFlex4
	@ShadowFlex4.setter
	def ShadowFlex4(self, new_state):
		self._setter_access_tracker["ShadowFlex4"] = {}
		self._ShadowFlex4 = ShadowFlex(new_state)

	@property
	def Input3(self):
		self._getter_access_tracker["Input3"] = {}
		return self._Input3
	@Input3.setter
	def Input3(self, new_state):
		self._setter_access_tracker["Input3"] = {}
		self._Input3 = Input(new_state)

	@property
	def NavFlex16(self):
		self._getter_access_tracker["NavFlex16"] = {}
		return self._NavFlex16
	@NavFlex16.setter
	def NavFlex16(self, new_state):
		self._setter_access_tracker["NavFlex16"] = {}
		self._NavFlex16 = NavFlex(new_state)

	@property
	def NavFlex17(self):
		self._getter_access_tracker["NavFlex17"] = {}
		return self._NavFlex17
	@NavFlex17.setter
	def NavFlex17(self, new_state):
		self._setter_access_tracker["NavFlex17"] = {}
		self._NavFlex17 = NavFlex(new_state)

	@property
	def NavFlex18(self):
		self._getter_access_tracker["NavFlex18"] = {}
		return self._NavFlex18
	@NavFlex18.setter
	def NavFlex18(self, new_state):
		self._setter_access_tracker["NavFlex18"] = {}
		self._NavFlex18 = NavFlex(new_state)

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
	def Flex22(self):
		self._getter_access_tracker["Flex22"] = {}
		return self._Flex22
	@Flex22.setter
	def Flex22(self, new_state):
		self._setter_access_tracker["Flex22"] = {}
		self._Flex22 = Flex(new_state)

	@property
	def TextBox33(self):
		self._getter_access_tracker["TextBox33"] = {}
		return self._TextBox33
	@TextBox33.setter
	def TextBox33(self, new_state):
		self._setter_access_tracker["TextBox33"] = {}
		self._TextBox33 = TextBox(new_state)

	@property
	def Flex23(self):
		self._getter_access_tracker["Flex23"] = {}
		return self._Flex23
	@Flex23.setter
	def Flex23(self, new_state):
		self._setter_access_tracker["Flex23"] = {}
		self._Flex23 = Flex(new_state)

	@property
	def TextBox34(self):
		self._getter_access_tracker["TextBox34"] = {}
		return self._TextBox34
	@TextBox34.setter
	def TextBox34(self, new_state):
		self._setter_access_tracker["TextBox34"] = {}
		self._TextBox34 = TextBox(new_state)

	@property
	def TextBox35(self):
		self._getter_access_tracker["TextBox35"] = {}
		return self._TextBox35
	@TextBox35.setter
	def TextBox35(self, new_state):
		self._setter_access_tracker["TextBox35"] = {}
		self._TextBox35 = TextBox(new_state)

	@property
	def Flex24(self):
		self._getter_access_tracker["Flex24"] = {}
		return self._Flex24
	@Flex24.setter
	def Flex24(self, new_state):
		self._setter_access_tracker["Flex24"] = {}
		self._Flex24 = Flex(new_state)

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
	def Anchor23(self):
		self._getter_access_tracker["Anchor23"] = {}
		return self._Anchor23
	@Anchor23.setter
	def Anchor23(self, new_state):
		self._setter_access_tracker["Anchor23"] = {}
		self._Anchor23 = Anchor(new_state)

	@property
	def Anchor24(self):
		self._getter_access_tracker["Anchor24"] = {}
		return self._Anchor24
	@Anchor24.setter
	def Anchor24(self, new_state):
		self._setter_access_tracker["Anchor24"] = {}
		self._Anchor24 = Anchor(new_state)

	@property
	def Anchor25(self):
		self._getter_access_tracker["Anchor25"] = {}
		return self._Anchor25
	@Anchor25.setter
	def Anchor25(self, new_state):
		self._setter_access_tracker["Anchor25"] = {}
		self._Anchor25 = Anchor(new_state)

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
	def TextBox36(self):
		self._getter_access_tracker["TextBox36"] = {}
		return self._TextBox36
	@TextBox36.setter
	def TextBox36(self, new_state):
		self._setter_access_tracker["TextBox36"] = {}
		self._TextBox36 = TextBox(new_state)

	@property
	def Image9(self):
		self._getter_access_tracker["Image9"] = {}
		return self._Image9
	@Image9.setter
	def Image9(self, new_state):
		self._setter_access_tracker["Image9"] = {}
		self._Image9 = Image(new_state)

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
	def TextBox37(self):
		self._getter_access_tracker["TextBox37"] = {}
		return self._TextBox37
	@TextBox37.setter
	def TextBox37(self, new_state):
		self._setter_access_tracker["TextBox37"] = {}
		self._TextBox37 = TextBox(new_state)

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
	def footer1(self):
		self._getter_access_tracker["footer1"] = {}
		return self._footer1
	@footer1.setter
	def footer1(self, new_state):
		self._setter_access_tracker["footer1"] = {}
		self._footer1 = Flex(new_state)
  
	def _to_json_fields(self):
		return {
			"TextBox1": self._TextBox1,
			"TextBox2": self._TextBox2,
			"TextBox3": self._TextBox3,
			"TextBox4": self._TextBox4,
			"TextBox5": self._TextBox5,
			"TextBox6": self._TextBox6,
			"ShadowFlex1": self._ShadowFlex1,
			"ShadowFlex2": self._ShadowFlex2,
			"NavFlex1": self._NavFlex1,
			"NavFlex2": self._NavFlex2,
			"NavFlex3": self._NavFlex3,
			"NavFlex4": self._NavFlex4,
			"Image1": self._Image1,
			"Anchor1": self._Anchor1,
			"Anchor2": self._Anchor2,
			"Dropdown1": self._Dropdown1,
			"Anchor3": self._Anchor3,
			"Anchor4": self._Anchor4,
			"Anchor5": self._Anchor5,
			"Anchor6": self._Anchor6,
			"Image2": self._Image2,
			"Anchor7": self._Anchor7,
			"Flex1": self._Flex1,
			"Flex2": self._Flex2,
			"Flex3": self._Flex3,
			"Flex4": self._Flex4,
			"Flex5": self._Flex5,
			"Flex6": self._Flex6,
			"navbar1": self._navbar1,
			"Flex8": self._Flex8,
			"Flex9": self._Flex9,
			"Flex10": self._Flex10,
			"Flex11": self._Flex11,
			"Flex12": self._Flex12,
			"Flex13": self._Flex13,
			"TextBox7": self._TextBox7,
			"TextBox8": self._TextBox8,
			"Flex14": self._Flex14,
			"Flex15": self._Flex15,
			"Image3": self._Image3,
			"Image4": self._Image4,
			"TextBox9": self._TextBox9,
			"TextBox10": self._TextBox10,
			"Anchor8": self._Anchor8,
			"Flex16": self._Flex16,
			"TextBox11": self._TextBox11,
			"Input1": self._Input1,
			"Input2": self._Input2,
			"TextBox12": self._TextBox12,
			"Flex17": self._Flex17,
			"Flex18": self._Flex18,
			"TextBox13": self._TextBox13,
			"Textarea1": self._Textarea1,
			"Flex19": self._Flex19,
			"Checkbox1": self._Checkbox1,
			"Flex20": self._Flex20,
			"ShadowFlex3": self._ShadowFlex3,
			"TextBox14": self._TextBox14,
			"FramerFlex1": self._FramerFlex1,
			"FramerFlex2": self._FramerFlex2,
			"FramerFlex3": self._FramerFlex3,
			"FramerFlex4": self._FramerFlex4,
			"Image5": self._Image5,
			"TextBox15": self._TextBox15,
			"Image6": self._Image6,
			"TextBox16": self._TextBox16,
			"Image7": self._Image7,
			"TextBox17": self._TextBox17,
			"TextBox18": self._TextBox18,
			"Image8": self._Image8,
			"TextBox19": self._TextBox19,
			"TextBox20": self._TextBox20,
			"TextBox21": self._TextBox21,
			"TextBox22": self._TextBox22,
			"TextBox23": self._TextBox23,
			"TextBox24": self._TextBox24,
			"TextBox25": self._TextBox25,
			"NavFlex5": self._NavFlex5,
			"NavFlex6": self._NavFlex6,
			"NavFlex7": self._NavFlex7,
			"NavFlex8": self._NavFlex8,
			"Anchor9": self._Anchor9,
			"Anchor10": self._Anchor10,
			"Anchor11": self._Anchor11,
			"Anchor12": self._Anchor12,
			"Anchor13": self._Anchor13,
			"Anchor14": self._Anchor14,
			"Anchor15": self._Anchor15,
			"TextBox26": self._TextBox26,
			"TextBox27": self._TextBox27,
			"TextBox28": self._TextBox28,
			"TextBox29": self._TextBox29,
			"TextBox30": self._TextBox30,
			"TextBox31": self._TextBox31,
			"TextBox32": self._TextBox32,
			"Anchor16": self._Anchor16,
			"Anchor17": self._Anchor17,
			"Anchor18": self._Anchor18,
			"Anchor19": self._Anchor19,
			"NavFlex9": self._NavFlex9,
			"NavFlex10": self._NavFlex10,
			"NavFlex11": self._NavFlex11,
			"NavFlex12": self._NavFlex12,
			"NavFlex13": self._NavFlex13,
			"NavFlex14": self._NavFlex14,
			"NavFlex15": self._NavFlex15,
			"ShadowFlex4": self._ShadowFlex4,
			"Input3": self._Input3,
			"NavFlex16": self._NavFlex16,
			"NavFlex17": self._NavFlex17,
			"NavFlex18": self._NavFlex18,
			"NavFlex19": self._NavFlex19,
			"NavFlex20": self._NavFlex20,
			"NavFlex21": self._NavFlex21,
			"Flex22": self._Flex22,
			"TextBox33": self._TextBox33,
			"Flex23": self._Flex23,
			"TextBox34": self._TextBox34,
			"TextBox35": self._TextBox35,
			"Flex24": self._Flex24,
			"Anchor20": self._Anchor20,
			"Anchor21": self._Anchor21,
			"Anchor22": self._Anchor22,
			"Anchor23": self._Anchor23,
			"Anchor24": self._Anchor24,
			"Anchor25": self._Anchor25,
			"Flex25": self._Flex25,
			"Flex26": self._Flex26,
			"Flex27": self._Flex27,
			"TextBox36": self._TextBox36,
			"Image9": self._Image9,
			"Flex28": self._Flex28,
			"Flex29": self._Flex29,
			"TextBox37": self._TextBox37,
			"Flex30": self._Flex30,
			"Flex31": self._Flex31,
			"Flex32": self._Flex32,
			"Flex33": self._Flex33,
			"Flex34": self._Flex34,
			"footer1": self._footer1
			}
  