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
  }
>((props, ref) => {

    const variants={
        initial:{

        },
        animate:{

        },
        whileHover:{
            color: props.custom.hoverColor,
            backgroundColor: props.custom.hoverBackgroundColor,
            boxShadow: `8px 8px 0px 0px #000000`,
            // boxShadow: `${props.custom.hoverHShadow}px ${props.custom.hoverVShadow}px ${props.custom.hoverBlurRadius}px ${props.custom.hoverSpreadRadius}px ${props.custom.hoverShadowColor}`,
            transition:{
                duration: props.custom.duration,
            }
        }
    }
  
  return (
    <motion.div
      ref={ref}
      style={{ ...props.styles, display: "flex", position: "relative" }}
      className={props.className}
      variants={variants}
      initial="initial"
      animate="animate"
      whileHover="whileHover"
    >
      {props.children}
    </motion.div>
  );
});

export default ShadowFlex;