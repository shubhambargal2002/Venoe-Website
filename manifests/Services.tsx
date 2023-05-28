import { ReactComponent as Icon } from "./hamburger.svg";
import React, { useCallback, useState } from "react";

const DropdownMenu = React.forwardRef<
	HTMLDivElement,
	{
		className: string;
		styles: React.CSSProperties;
		children: React.ReactNode[];
		custom: {
			src?: string;
			iconWidth?: number;
			iconHeight?: number;
            text?: string;
		};
		id?: string;
	}
>((props, ref) => {
	const [open, setOpen] = useState<boolean>(false);
	const onClickCb = useCallback(() => {
		setOpen((open) => !open);
	}, []);
	return (
		<div
			ref={ref}
			className={props.className}
			id={props.id}
			style={{
				...props.styles,
				position: "relative",
				display: "flex",
				alignItems: "center",
				justifyContent: "center",
			}}
			onClick={onClickCb}
		>
            <div style={{...props.styles, display:"flex", flexDirection:"row",columnGap:"10px", alignItems:"center", cursor:"pointer"}}>
                <div>{props.custom.text}</div>
				<div>{props.custom.src ? (
					<img
						src={props.custom.src}
						height={props.custom.iconHeight}
						width={props.custom.iconWidth}
					></img>
				) : (
					<Icon />
				)}</div>
            </div>
			<div
				style={{
					position: "absolute",
					top: "3em",
					right: "0",
					zIndex: 1
				}}
			>
				{open ? props.children : null}
			</div>
		</div>
	);
});

export default DropdownMenu;
