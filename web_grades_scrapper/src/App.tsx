import './App.css'
import React, {useState} from "react";
import {Field, FormikProvider, useFormik} from 'formik';

const App: React.FC = () => {
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
    )
}

export default App
