

export interface ListData {
    "name": string,
    "page_name": string
}

export interface DetailData {
    "url": string
}

export interface PropsList {
    handleNavigation: (url: string, page: string) => void,
    data: any[]
}
