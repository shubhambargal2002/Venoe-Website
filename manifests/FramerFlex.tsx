import React, { forwardRef, useImperativeHandle, useRef } from "react";
import { motion, useInView } from "framer-motion";

export const FramerFlex = forwardRef<
	HTMLDivElement,
	{
		styles: React.CSSProperties;
		children: React.ReactNode[];
		custom: {
			duration?: number;
			delay?: number;
		};
		className?: string;
		id?: string;
	}
>((props, ref) => {
	const internalRef = useRef<HTMLDivElement>(null);
	useImperativeHandle(ref, () => internalRef.current!);
	const inView = useInView(internalRef, { once: true });

	return (
		<motion.div
			ref={internalRef}
			style={{
				...props.styles,
				display: "flex",
				position: "relative",
				transform: inView ? `scale(1)` : `scale(0)`,
				transition: `all ${props.custom.duration}s cubic-bezier(0.17, 0.55, 0.55, 1) ${props.custom.delay}s`,
			}}
			id={props.id}
			className={props.className}
		>
			{props.children}
		</motion.div>
	);
});

export default FramerFlex;
