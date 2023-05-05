import { createComponentManifest } from "@atrilabs/utils";

export default createComponentManifest({
	name: "FramerFlex",
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
        initialScale: { type: "number" },
        finalScale: { type: "number" },
        duration: { type: "number" },
        delay: { type: "number" }
	},

	initalCustomValues: {
        initialScale: 0,
        finalScale: 0,
        duration: 0,
        delay: 0
	},
});