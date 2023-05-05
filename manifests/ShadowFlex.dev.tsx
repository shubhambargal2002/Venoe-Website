import ShadowFlex from "./ShadowFlex";
import React from "react";

const DevShadowFlex: typeof ShadowFlex =
	React.forwardRef((props, ref) => {
		const overrideStyles =
			props.children.length === 0
				? {
						height: "100px",
						border: "1px dashed red",
                        minWidth: "100px"
				  }
				: props.styles;
		return (
			<ShadowFlex
				ref={ref}
				{...props}
				styles={overrideStyles}
			/>
		);
	});

export default DevShadowFlex;