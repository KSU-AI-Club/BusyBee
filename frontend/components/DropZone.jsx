import React from "react";
import { useDropzone } from "react-dropzone";
import "../assets/css/DropZone.css";

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

  return (
    <section className="container">
      <div className="dropZone">
        <div {...getRootProps({ className: "dropzone" })}>
          <input {...getInputProps()} />
          <p>Drag 'n' drop some files here</p>
          <em>(Only *.jpeg and *.png images will be accepted)</em>
          <br></br>
          <br></br>
          <button type="button" onClick={open}>
            Open File Dialog
          </button>
          <br></br>
          <br></br>
        </div>
      </div>

      <aside>
        <h4>Files:</h4>
        <ul>{files}</ul>
        {files.length > 0 ? (
          <button type="button" title="submitButton">
            Submit
          </button>
        ) : null}
      </aside>
    </section>
  );
}

<DropZone />;

export default DropZone;
