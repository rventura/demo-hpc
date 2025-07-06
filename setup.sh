if command -v ml &> /dev/null ; then
    echo "Loading modules."
    ml Python
    ml OpenMPI
fi

source ./env/bin/activate
