import React, { forwardRef, useRef } from "react";
import { motion, useInView } from "framer-motion";

export const FramerFlex = forwardRef<
  HTMLDivElement,
  {
    styles: React.CSSProperties;
    children: React.ReactNode[];
    custom: {
        initialScale?: number,
        finalScale?: number,
        duration?: number,
        delay?: number
    };
    className?: string;
  }
>((props, ref) => {

  const variants={
    initial:{
      // scale:props.custom.initialScale,
      scale:0
    },
    animate:{
      // scale:props.custom.finalScale,
      scale:1,
      transition:{
        // duration:props.custom.duration,
        // delay:props.custom.delay
        duration:1,
        delay:0
      }
    }
  }
  
  return (
    <motion.div
      ref={ref}
      style={{ ...props.styles, display: "flex", position: "relative"}}
      className={props.className}
      variants={variants}
      initial="initial"
      animate="animate"
    >
        {props.children}
    </motion.div>
  );
});

export default FramerFlex;