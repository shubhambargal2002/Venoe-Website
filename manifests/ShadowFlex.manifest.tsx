import { createComponentManifest } from "@atrilabs/utils";

export default createComponentManifest({
	name: "ShadowFlex",
	acceptsChild: "flex",
    styles:{
        boxShadowOptions: true,
        flexContainerOptions: true,
        flexChildOptions: true,
        positionOptions: true,
        typographyOptions: true,
        spacingOptions: true,
        sizeOptions: true,
        borderOptions: true,
        outlineOptions: true,
        backgroundOptions: true,
        miscellaneousOptions: true,
    },

	custom: {
        duration: { type: "number" },
        hoverHShadow: { type: "number" },
        hoverVShadow: { type: "number" },
        hoverBlurRadius: { type: "number" },
        hoverSpreadRadius: { type: "number" },
        hoverShadowColor: { type: "color" },
        hoverColor: { type: "color" },
        hoverBackgroundColor: { type: "color" }
	},

	initalCustomValues: {
        duration: 0,
        hoverHShadow: 0,
        hoverVShadow: 0,
        hoverBlurRadius: 0,
        hoverSpreadRadius: 0,
        hoverShadowColor: "#000000",
        hoverColor: "",
        hoverBackgroundColor: ""
	},
});