import React, {useState} from "react";
import ReactLoading from 'react-loading';
import {Field, FormikProvider, FormikValues, useFormik} from 'formik';
import {useGetListData} from "./mutations.tsx";
import ListDataComponent from "./ListDataComponent.tsx";


const App: React.FC = () => {
    const [page, setPage] = useState<string>("opencritic")
    const {data: ListData, mutate: mutateListData, isLoading: isLoadingListData} = useGetListData()
    const formik = useFormik({
        initialValues: {
            inputField: '',
            type: 'all_items',
            page: 'opencritic'
        },
        onSubmit: (values) => {
            if (values.page == "opencritic") {
                mutateListData({"name": values.inputField, "page_name": "opencritic"})
                setPage("opencritic")
            } else if (values.page == "metacritic") {
                mutateListData({"name": values.inputField, "page_name": "metacritic"})
                setPage("metacritic")
            } else if (values.page == "imdb") {
                mutateListData({"name": values.inputField, "page_name": "imdb"})
                setPage("imdb")
            }
        }
    })
    return (
        <>
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
            {isLoadingListData && <ReactLoading height={'20%'} width={'20%'}/>}
            {ListData && <ListDataComponent data={ListData} page={page}/>}
        </>
    )
}

export default App
