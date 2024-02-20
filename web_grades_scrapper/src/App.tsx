import React, {useState} from "react";
import ReactLoading from 'react-loading';
import {Field, FormikProvider, useFormik} from 'formik';
import {useGetListData} from "./mutations.tsx";
import ListDataComponent from "./ListDataComponent.tsx";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";


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
        <div className="w-full items-center flex text-white flex flex-col h-full">
            <div className="form_container w-full h-1/2 flex justify-center">

                <FormikProvider value={formik}>
                    <form className="w-full justify-center items-center flex flex-col"
                          onSubmit={formik.handleSubmit}>
                        <p className="text-center text-3xl mb-5">Wyszukiwarka ocen</p>
                        <div className="w-1/2 flex justify-center input_field mb-5">
                            <input
                                className="w-full py-2 px-3 rounded-lg text-lg md:mr-3 border-2 rounded-lg border-white text-black"
                                id="inputField"
                                type="text"
                                onChange={formik.handleChange}
                                value={formik.values.inputField}
                            />
                        </div>
                        <div className="radio_fields text-xl " role="group" aria-labelledby="my-radio-group">
                            <label className="mr-5">
                                <Field checked="checked" type="radio" name="page" value="opencritic"/>
                                Opencritic
                            </label>
                            <label className="mr-5">
                                <Field type="radio" name="page" value="metacritic" className="ml-2"/>
                                Metacritic
                            </label>
                            <label>
                                <Field type="radio" name="page" value="imdb"/>
                                Imdb
                            </label>
                        </div>
                        <button className="mt-5 py-3 px-5 border rounded-lg hover:border-blue-700 hover:text-blue-700" type="submit">Submit</button>
                    </form>
                </FormikProvider>
            </div>
            <div className="results w-full h-1/2 flex justify-center">
                {isLoadingListData && <ReactLoading height={'10%'} width={'10%'}/>}
                {ListData && <ListDataComponent data={ListData} page={page}/>}
            </div>
        </div>
    )
}

export default App
