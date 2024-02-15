// import PropTypes from 'prop-types';
import {PropsList} from "../interfaces.tsx";

function MetacriticList(props: PropsList) {
    // const list_of_metacritic_elements = props.data.map((element) => <div
    //     onClick={() => props.handleNavigation(element.url, "metacritic")} key={element.id}>{element.name}</div>)
    const list_of_metacritic_elements = props.data.map((element) =>
        // <div onClick={() => props.handleNavigation(element.url, "metacritic")} key={element.id}>{element.name}</div>
        <li className="py-3 sm:pb-4 cursor-pointer" onClick={() => props.handleNavigation(element.url, "metacritic")}>
            <div className="flex items-center space-x-4 rtl:space-x-reverse">
                <div className="flex-shrink-0">
                    {element.img ? <img className="w-14 h-14 rounded-full" src={element.img}
                                        alt=""/> :
                        <img className="w-14 h-14 rounded-full" src="/no_image.jpg" alt="no_image"/>}
                </div>
                <div className="flex-1 min-w-0">
                    <p className="text-sm font-medium text-gray-900 truncate dark:text-white">
                        {element.name}
                    </p>
                    <p className="text-sm text-gray-500 truncate dark:text-gray-400">
                        {element.year} {element.platforms}
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
                className="divide-y divide-gray-200 dark:divide-gray-700"
            >
                {list_of_metacritic_elements}
            </ul>

        </>
    )
};

// MetacriticList.propTypes = {
//     handleNavigation: PropTypes.func,
//     data: PropTypes.array
// };

export default MetacriticList;
