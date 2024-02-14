import {PropsList} from "../interfaces.tsx";

// import PropTypes from 'prop-types';

function ImdbList(props: PropsList) {
    const list_of_imdb_elements = props.data.map((element) =>
        <li className="py-3 sm:pb-4 cursor-pointer" onClick={() => props.handleNavigation(element.url, "imdb")}>
            <div className="flex items-center space-x-4 rtl:space-x-reverse">
                <div className="flex-shrink-0">
                    {element.img ? <img className="w-14 h-14 rounded-full" src={element.img}
                                        alt=""/> :
                        <img className="w-14 h-14 rounded-full" src="/no_image.jpg" alt="no_image"/>}
                </div>
                <div className="flex-1 min-w-0">
                    <p className="text-sm font-medium text-gray-900 truncate dark:text-white">
                        {element.title}
                    </p>
                    <p className="text-sm text-gray-500 truncate dark:text-gray-400">
                        {element.description.map((el: string) => {
                            return (<span>{el} </span>)
                        })}
                    </p>
                </div>
                <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">
                    {element.metascore}
                </div>
            </div>
        </li>
    )
    return (
        <>
            <ul
                className="w-4/5 lg:w-2/5 divide-y divide-gray-200 dark:divide-gray-700"
            >
                {list_of_imdb_elements}
            </ul>
        </>
    )
};


export default ImdbList;
