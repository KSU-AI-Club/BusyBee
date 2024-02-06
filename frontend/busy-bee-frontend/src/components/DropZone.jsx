import React from "react";
import { ReactDOM } from "react";
import { useDropzone } from "react-dropzone";
import "./frontend/assets/DropZone.css";

function DropZone(props) {
  const { acceptedFiles, open, getRootProps, getInputProps } = useDropzone({
    noClick: true,
    accept: {
      "image/jpeg": [],
      "image/png": [],
    },
  });

  const files = acceptedFiles.map((file) => (
    <li key={file.path}>
      {file.path} - {file.size} bytes
    </li>
  ));

  
}

<DropZone />;

export default DropZone;
