import React, { forwardRef, useImperativeHandle, useRef } from "react";
import { motion, useInView, useScroll } from "framer-motion";

export const FramerFlex = forwardRef<
	HTMLDivElement,
	{
		styles: React.CSSProperties;
		children: React.ReactNode[];
		custom: {
			initialScale?: number;
			finalScale?: number;
			duration?: number;
			delay?: number;
		};
		className?: string;
	}
>((props, ref) => {
	const internalRef = useRef<HTMLDivElement>(null);
	useImperativeHandle(ref, () => internalRef.current!);
	const inView = useInView(internalRef, { once: true });

	const variants = {
		initial: {
			// scale:props.custom.initialScale,
			scale: 0,
		},
		animate: {
			// scale:props.custom.finalScale,
			scale: 1,
			transition: {
				// duration:props.custom.duration,
				// delay:props.custom.delay
				duration: 1,
				delay: 0,
			},
		},
	};

	return (
		<motion.div
			ref={internalRef}
			style={{
				...props.styles,
				display: "flex",
				position: "relative",
				transform: inView ? `scale(1)` : `scale(0)`,
				transition: "all 0.9s cubic-bezier(0.17, 0.55, 0.55, 1) 0.5s",
			}}
			className={props.className}
		>
			{props.children}
		</motion.div>
	);
});

export default FramerFlex;
