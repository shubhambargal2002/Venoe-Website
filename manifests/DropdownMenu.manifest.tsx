import { createComponentManifest } from "@atrilabs/utils";

export default createComponentManifest({
	name: "DropdownMenu",
	acceptsChild: () => {
		return 0;
	},
	custom: {
		src: { type: "static_asset" },
		iconWidth: { type: "number" },
		iconHeight: { type: "number" },
	},
	styles: {
		sizeOptions: true,
		spacingOptions: true,
	},
});
