import axios from "axios";
import ListData from "./interfaces.tsx"
import DetailData from "./interfaces.tsx"
const instance = axios.create();


export async function  getOpencriticListData(data: ListData){
    const response = await instance.post(`http://0.0.0.0:8000/opencritic`, data);
    return response.data;
}

export async function  getMetacriticListData(data: ListData){
    const response = await instance.post(`http://0.0.0.0:8000/metacritic`, data);
    return response.data;
}

export async function  getImdbListData(data: ListData){
    const response = await instance.post(`http://0.0.0.0:8000/imdb`, data);
    return response.data;
}


export async function  getOpencriticDetailData(data: DetailData){
    const response = await instance.post(`http://0.0.0.0:8000/opencritic_detail`, data);
    return response.data;
}

export async function  getMetacriticDetailData(data: DetailData){
    const response = await instance.post(`http://0.0.0.0:8000/metacritic_detail`, data);
    return response.data;
}

export async function  getImdbDetailData(data: DetailData){
    const response = await instance.post(`http://0.0.0.0:8000/imdb_detail`, data);
    return response.data;
}