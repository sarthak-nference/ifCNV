#!/bin/bash

# Path where the tarball is extracted
EXTRACT_DIR="ifCNV"

# Path to the Python executable (adjust as needed)
PYTHON_EXEC=$(which python3)

# Check if Python is available
if [ -z "$PYTHON_EXEC" ]; then
  echo "Python 3 is not installed or not found in PATH."
  exit 1
fi

# Create the ifCNV executable wrapper in the repository
EXEC_WRAPPER="$EXTRACT_DIR/ifCNV"

echo "Creating the ifCNV executable wrapper script..."

# Create the wrapper script
cat <<EOF > $EXEC_WRAPPER
#!/bin/bash
IF_CNV_DIR="\$(dirname "\$0")"
\$PYTHON_EXEC \$IF_CNV_DIR/ifCNV "\$@"
EOF

# Make the wrapper executable
chmod +x $EXEC_WRAPPER

echo "Executable wrapper created at $EXEC_WRAPPER"
