import React, { forwardRef } from "react";
import { motion } from "framer-motion";

export const ShadowFlex = forwardRef<
  HTMLDivElement,
  {
    styles: React.CSSProperties;
    children: React.ReactNode[];
    custom: {
        duration?: number,
        hoverHShadow?: number,
        hoverVShadow?: number,
        hoverBlurRadius?: number,
        hoverSpreadRadius?: number,
        hoverShadowColor?: string,
        hoverColor?: string,
        hoverBackgroundColor?: string
    };
    className?: string;
    id?: string;
  }
>((props, ref) => {

    const variants={
        whileHover:{
            color: props.custom.hoverColor,
            backgroundColor: props.custom.hoverBackgroundColor,
            boxShadow: `${props.custom.hoverHShadow}px ${props.custom.hoverVShadow}px ${props.custom.hoverBlurRadius}px ${props.custom.hoverSpreadRadius}px ${props.custom.hoverShadowColor}`,
            transition:{
                duration: props.custom.duration,
            }
        }
    }
  
  return (
    <motion.div
      ref={ref}
      style={{ ...props.styles, display: "flex", position: "relative" }}
      id={props.id}
      className={props.className}
      variants={variants}
      whileHover="whileHover"
    >
      {props.children}
    </motion.div>
  );
});

export default ShadowFlex;