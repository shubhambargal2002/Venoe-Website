from typing import Union, Any
from atri_react.TextBox import TextBox
from atri_react.Image import Image
from manifests.ShadowFlex import ShadowFlex
from atri_react.Input import Input
from atri_react.Anchor import Anchor
from atri_react.Div import Div
from atri_react.Flex import Flex


  
class Page:
	def __init__(self, state: Union[Any, None]):
		self.event_data = None
		self.event_alias = None
		self._setter_access_tracker = {}
		self.TextBox1 = state["TextBox1"] if "TextBox1" in state else None
		self.Image1 = state["Image1"] if "Image1" in state else None
		self.TextBox2 = state["TextBox2"] if "TextBox2" in state else None
		self.Image2 = state["Image2"] if "Image2" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
		self.TextBox3 = state["TextBox3"] if "TextBox3" in state else None
		self.TextBox4 = state["TextBox4"] if "TextBox4" in state else None
		self.TextBox5 = state["TextBox5"] if "TextBox5" in state else None
		self.ShadowFlex1 = state["ShadowFlex1"] if "ShadowFlex1" in state else None
		self.ShadowFlex2 = state["ShadowFlex2"] if "ShadowFlex2" in state else None
		self.ShadowFlex3 = state["ShadowFlex3"] if "ShadowFlex3" in state else None
		self.TextBox6 = state["TextBox6"] if "TextBox6" in state else None
		self.TextBox7 = state["TextBox7"] if "TextBox7" in state else None
		self.ShadowFlex4 = state["ShadowFlex4"] if "ShadowFlex4" in state else None
		self.Input1 = state["Input1"] if "Input1" in state else None
		self.Input2 = state["Input2"] if "Input2" in state else None
		self.Anchor1 = state["Anchor1"] if "Anchor1" in state else None
		self.TextBox8 = state["TextBox8"] if "TextBox8" in state else None
		self.Anchor2 = state["Anchor2"] if "Anchor2" in state else None
		self.Anchor3 = state["Anchor3"] if "Anchor3" in state else None
		self.Anchor4 = state["Anchor4"] if "Anchor4" in state else None
		self.TextBox9 = state["TextBox9"] if "TextBox9" in state else None
		self.Div1 = state["Div1"] if "Div1" in state else None
		self.Flex1 = state["Flex1"] if "Flex1" in state else None
		self.Flex2 = state["Flex2"] if "Flex2" in state else None
		self.Flex3 = state["Flex3"] if "Flex3" in state else None
		self.Flex4 = state["Flex4"] if "Flex4" in state else None
		self.Image4 = state["Image4"] if "Image4" in state else None
		self.Flex5 = state["Flex5"] if "Flex5" in state else None
		self.Flex6 = state["Flex6"] if "Flex6" in state else None
		self.Flex7 = state["Flex7"] if "Flex7" in state else None
		self.Flex8 = state["Flex8"] if "Flex8" in state else None
		self.register1 = state["register1"] if "register1" in state else None
		self.Flex10 = state["Flex10"] if "Flex10" in state else None
		self.TextBox10 = state["TextBox10"] if "TextBox10" in state else None
		self.Anchor5 = state["Anchor5"] if "Anchor5" in state else None
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
	def Image1(self):
		self._getter_access_tracker["Image1"] = {}
		return self._Image1
	@Image1.setter
	def Image1(self, new_state):
		self._setter_access_tracker["Image1"] = {}
		self._Image1 = Image(new_state)

	@property
	def TextBox2(self):
		self._getter_access_tracker["TextBox2"] = {}
		return self._TextBox2
	@TextBox2.setter
	def TextBox2(self, new_state):
		self._setter_access_tracker["TextBox2"] = {}
		self._TextBox2 = TextBox(new_state)

	@property
	def Image2(self):
		self._getter_access_tracker["Image2"] = {}
		return self._Image2
	@Image2.setter
	def Image2(self, new_state):
		self._setter_access_tracker["Image2"] = {}
		self._Image2 = Image(new_state)

	@property
	def Image3(self):
		self._getter_access_tracker["Image3"] = {}
		return self._Image3
	@Image3.setter
	def Image3(self, new_state):
		self._setter_access_tracker["Image3"] = {}
		self._Image3 = Image(new_state)

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
	def ShadowFlex3(self):
		self._getter_access_tracker["ShadowFlex3"] = {}
		return self._ShadowFlex3
	@ShadowFlex3.setter
	def ShadowFlex3(self, new_state):
		self._setter_access_tracker["ShadowFlex3"] = {}
		self._ShadowFlex3 = ShadowFlex(new_state)

	@property
	def TextBox6(self):
		self._getter_access_tracker["TextBox6"] = {}
		return self._TextBox6
	@TextBox6.setter
	def TextBox6(self, new_state):
		self._setter_access_tracker["TextBox6"] = {}
		self._TextBox6 = TextBox(new_state)

	@property
	def TextBox7(self):
		self._getter_access_tracker["TextBox7"] = {}
		return self._TextBox7
	@TextBox7.setter
	def TextBox7(self, new_state):
		self._setter_access_tracker["TextBox7"] = {}
		self._TextBox7 = TextBox(new_state)

	@property
	def ShadowFlex4(self):
		self._getter_access_tracker["ShadowFlex4"] = {}
		return self._ShadowFlex4
	@ShadowFlex4.setter
	def ShadowFlex4(self, new_state):
		self._setter_access_tracker["ShadowFlex4"] = {}
		self._ShadowFlex4 = ShadowFlex(new_state)

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
	def Anchor1(self):
		self._getter_access_tracker["Anchor1"] = {}
		return self._Anchor1
	@Anchor1.setter
	def Anchor1(self, new_state):
		self._setter_access_tracker["Anchor1"] = {}
		self._Anchor1 = Anchor(new_state)

	@property
	def TextBox8(self):
		self._getter_access_tracker["TextBox8"] = {}
		return self._TextBox8
	@TextBox8.setter
	def TextBox8(self, new_state):
		self._setter_access_tracker["TextBox8"] = {}
		self._TextBox8 = TextBox(new_state)

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
	def TextBox9(self):
		self._getter_access_tracker["TextBox9"] = {}
		return self._TextBox9
	@TextBox9.setter
	def TextBox9(self, new_state):
		self._setter_access_tracker["TextBox9"] = {}
		self._TextBox9 = TextBox(new_state)

	@property
	def Div1(self):
		self._getter_access_tracker["Div1"] = {}
		return self._Div1
	@Div1.setter
	def Div1(self, new_state):
		self._setter_access_tracker["Div1"] = {}
		self._Div1 = Div(new_state)

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
	def Image4(self):
		self._getter_access_tracker["Image4"] = {}
		return self._Image4
	@Image4.setter
	def Image4(self, new_state):
		self._setter_access_tracker["Image4"] = {}
		self._Image4 = Image(new_state)

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
	def register1(self):
		self._getter_access_tracker["register1"] = {}
		return self._register1
	@register1.setter
	def register1(self, new_state):
		self._setter_access_tracker["register1"] = {}
		self._register1 = Flex(new_state)

	@property
	def Flex10(self):
		self._getter_access_tracker["Flex10"] = {}
		return self._Flex10
	@Flex10.setter
	def Flex10(self, new_state):
		self._setter_access_tracker["Flex10"] = {}
		self._Flex10 = Flex(new_state)

	@property
	def TextBox10(self):
		self._getter_access_tracker["TextBox10"] = {}
		return self._TextBox10
	@TextBox10.setter
	def TextBox10(self, new_state):
		self._setter_access_tracker["TextBox10"] = {}
		self._TextBox10 = TextBox(new_state)

	@property
	def Anchor5(self):
		self._getter_access_tracker["Anchor5"] = {}
		return self._Anchor5
	@Anchor5.setter
	def Anchor5(self, new_state):
		self._setter_access_tracker["Anchor5"] = {}
		self._Anchor5 = Anchor(new_state)
  
	def _to_json_fields(self):
		return {
			"TextBox1": self._TextBox1,
			"Image1": self._Image1,
			"TextBox2": self._TextBox2,
			"Image2": self._Image2,
			"Image3": self._Image3,
			"TextBox3": self._TextBox3,
			"TextBox4": self._TextBox4,
			"TextBox5": self._TextBox5,
			"ShadowFlex1": self._ShadowFlex1,
			"ShadowFlex2": self._ShadowFlex2,
			"ShadowFlex3": self._ShadowFlex3,
			"TextBox6": self._TextBox6,
			"TextBox7": self._TextBox7,
			"ShadowFlex4": self._ShadowFlex4,
			"Input1": self._Input1,
			"Input2": self._Input2,
			"Anchor1": self._Anchor1,
			"TextBox8": self._TextBox8,
			"Anchor2": self._Anchor2,
			"Anchor3": self._Anchor3,
			"Anchor4": self._Anchor4,
			"TextBox9": self._TextBox9,
			"Div1": self._Div1,
			"Flex1": self._Flex1,
			"Flex2": self._Flex2,
			"Flex3": self._Flex3,
			"Flex4": self._Flex4,
			"Image4": self._Image4,
			"Flex5": self._Flex5,
			"Flex6": self._Flex6,
			"Flex7": self._Flex7,
			"Flex8": self._Flex8,
			"register1": self._register1,
			"Flex10": self._Flex10,
			"TextBox10": self._TextBox10,
			"Anchor5": self._Anchor5
			}
  