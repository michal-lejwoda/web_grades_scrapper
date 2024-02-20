import axios from "axios";
import {ListData} from "./interfaces.tsx"
import {DetailData} from "./interfaces.tsx"
const instance = axios.create();


export async function getListData(data: ListData){
    let response
    switch (data.page_name){
        case 'opencritic':
            response = await instance.post(`/api/opencritic`, data);
            return response.data;
        case 'metacritic':
            response = await instance.post(`/api/metacritic`, data);
            return response.data;
        case 'imdb':
            response = await instance.post(`/api/imdb`, data);
            return response.data;
    }
}

export async function  getOpencriticDetailData(data: DetailData){
    const response = await instance.post(`/api/opencritic_detail`, data);
    return response.data;
}

export async function  getMetacriticDetailData(data: DetailData){
    const response = await instance.post(`/api/metacritic_detail`, data);
    return response.data;
}

export async function  getImdbDetailData(data: DetailData){
    const response = await instance.post(`/api/imdb_detail`, data);
    return response.data;
}