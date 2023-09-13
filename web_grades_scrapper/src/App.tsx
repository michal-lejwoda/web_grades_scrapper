// import './App.css'
import React, {useState} from "react";
import {Field, FormikProvider, useFormik} from 'formik';
import {useMutation} from 'react-query'
import {getImdbListData, getMetacriticListData, getOpencriticListData} from "./api.tsx";


const App: React.FC = () => {
    const [list_of_elements, setListOfElements] = useState()
    // mutations
    const getOpencriticList = useMutation(getOpencriticListData, {
        onSuccess: (data) =>{
            console.log(data)
        }
    })

    const getMetacriticList = useMutation(getMetacriticListData, {
        onSuccess: (data) =>{
            console.log(data)
        }
    })

    const getImdbList = useMutation(getImdbListData, {
        onSuccess: (data) =>{
            console.log(data)
        }
    })
    const [formdata, setFormData] = useState()

    const formik = useFormik({
        initialValues: {
            inputField: '',
            type: 'all_items',
            page: 'opencritic'
        },
        onSubmit: (values) => {
            if (values.page == "opencritic"){
               getOpencriticList.mutate({"name": values.inputField})
            }else if(values.page == "metacritic"){
                getMetacriticList.mutate({"name": values.inputField})
            }else if(values.page == "imdb"){
                getImdbList.mutate({"name": values.inputField})
            }
        }
    })
    return (
        <>
            <h1>Test App reload</h1>
            <FormikProvider value={formik}>
                <form onSubmit={formik.handleSubmit}>
                    <input
                        id="inputField"
                        type="text"
                        onChange={formik.handleChange}
                        value={formik.values.inputField}
                    />
                    <div role="group" aria-labelledby="my-radio-group">
                        <label>
                            <Field checked="checked" type="radio" name="type" value="all_items"/>
                            All items
                        </label>
                        <label>
                            <Field type="radio" name="type" value="movie"/>
                            Movie
                        </label>
                        <label>
                            <Field type="radio" name="type" value="game"/>
                            Game
                        </label>
                        <label>
                            <Field type="radio" name="type" value="album"/>
                            Album
                        </label>
                    </div>


                    <div role="group" aria-labelledby="my-radio-group">
                        <label>
                            <Field checked="checked" type="radio" name="page" value="opencritic"/>
                            Opencritic
                        </label>
                        <label>
                            <Field type="radio" name="page" value="metacritic"/>
                            Metacritic
                        </label>
                        <label>
                            <Field type="radio" name="page" value="imdb"/>
                            Imdb
                        </label>
                    </div>
                    <button type="submit">Submit</button>
                </form>
            </FormikProvider>
        </>
    )
}

export default App
