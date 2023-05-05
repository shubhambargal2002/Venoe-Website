import NavFlex from "./NavFlex";
import React from "react";

const DevNavFlex: typeof NavFlex =
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
			<NavFlex
				ref={ref}
				{...props}
				styles={overrideStyles}
			/>
		);
	});

export default DevNavFlex;