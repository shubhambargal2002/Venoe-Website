import { createComponentManifest } from "@atrilabs/utils";

export default createComponentManifest({
	name: "NavFlex",
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
        hoverColor: { type: "color" },
        x: { type: "number" },
        duration: { type: "number" },
	},

	initalCustomValues: {
        hoverColor: "",
        x: 0,
        duration: 0,
	},
});