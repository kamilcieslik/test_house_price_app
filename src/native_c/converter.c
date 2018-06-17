#include <Python.h>

static PyObject* converter_sum_of_squares(PyObject *self, PyObject
        *args){
    /* Declare the variables */
    int n;
    int sum = 0;

    /* Parse the arguments */
    if(!PyArg_ParseTuple(args, "i", &n)){
        return NULL;
    }

    /* The actual summing code */
    for(int i=0; i<n; i++){
        if((i * i) < n){
            sum += i * i;
        }else{
            break;
        }
    }

    /* Return the number but convert it to a Python object first
     */
    return PyLong_FromLong(sum);
}

static PyMethodDef converter_methods[] = {
    /* Register the function */
    {"sum_of_squares", converter_sum_of_squares, METH_VARARGS,
     "Sum the perfect squares below n"},
    /* Indicate the end of the list */
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef converter_module = {
    PyModuleDef_HEAD_INIT,
    "converter", /* Module name */
    NULL, /* Module documentation */
    -1, /* Module state, -1 means global. This parameter is
           for sub-interpreters */
    converter_methods,
};

/* Initialize the module */
PyMODINIT_FUNC PyInit_converter(void){
    return PyModule_Create(&converter_module);
}