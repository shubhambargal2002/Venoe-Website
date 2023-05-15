import { createComponentManifest } from "@atrilabs/utils";

export default createComponentManifest({
	name: "Services",
	acceptsChild: () => {
		return 0;
	},
	custom: {
		src: { type: "static_asset" },
		iconWidth: { type: "number" },
		iconHeight: { type: "number" },
        text: { type : "text"}
	},
	styles: {
		sizeOptions: true,
		spacingOptions: true,
	},
});
