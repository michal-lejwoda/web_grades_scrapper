import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import {QueryClient, QueryClientProvider} from "react-query";
import {Route, Routes, BrowserRouter} from "react-router-dom";
import DetailComponent from "./DetailComponent.tsx";

const queryClient = new QueryClient()

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <QueryClientProvider client={queryClient}>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<App/>}></Route>
                    <Route path="/detail" element={<DetailComponent/>}></Route>
                </Routes>
            </BrowserRouter>
            {/*<App />*/}
        </QueryClientProvider>
    </React.StrictMode>,
)
