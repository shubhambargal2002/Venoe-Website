import { createComponentManifest } from "@atrilabs/utils";

export default createComponentManifest({
	name: "Services",
	acceptsChild: () => {
		return 0;
	},

	styles : {
        boxShadowOptions: true,
        flexContainerOptions: false,
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
		src: { type: "static_asset" },
		iconWidth: { type: "number" },
		iconHeight: { type: "number" },
        text: { type : "text"}
	},
});
