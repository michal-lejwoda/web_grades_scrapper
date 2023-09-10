import './App.css'
import React, {useState} from "react";
import {Field, FormikProvider, useFormik} from 'formik';
import {QueryClient, QueryClientProvider, useQuery} from 'react-query'
import {
    useImdbDetailQuery,
    useImdbListQuery, useMetacriticDetailQuery,
    useMetacriticListQuery,
    useOpencriticDetailQuery,
    useOpencriticListQuery
} from "./hooks.tsx";


const queryClient = new QueryClient()
const App: React.FC = () => {

    const [formdata, setFormData] = useState({
        inputField: '',
        type: 'all_items',
        page: 'opencritic'
    })

    const handleMetacriticList = () => {
        const metacritic_list = useMetacriticListQuery()
    }

    const handleOpencriticList = () => {
        useOpencriticListQuery()
    }

    const handleImdbList = () => {
        useImdbListQuery()
    }

    const handleMetacriticDetail = () => {
        useMetacriticDetailQuery()
    }

    const handleOpencriticDetail = () => {
        useOpencriticDetailQuery()
    }

    const handleImdbDetail = () => {
        useImdbDetailQuery()
    }


    // const [count, setCount] = useState<string>("")
    const formik = useFormik({
        initialValues: {
            inputField: '',
            type: 'all_items',
            page: 'opencritic'
        },
        onSubmit: values => {
            console.log(values)
            alert("Submit")
        }
    })
    return (
        <QueryClientProvider client={queryClient}>
            <FormikProvider value={formik}>
                <form onSubmit={formik.handleSubmit}>
                    {/*<label htmlFor="email">Email Address</label>*/}
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
                        {/*<div>Picked: {formik.values.type}</div>*/}
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
                        <div>Picked: {formik.values.type}</div>
                        <div>Picked2: {formik.values.page}</div>
                    </div>
                    <button type="submit">Submit</button>
                </form>
            </FormikProvider>
        </QueryClientProvider>
    )
}

export default App
