// import PropTypes from 'prop-types';
import {PropsList} from "../interfaces.tsx";


function OpencriticList(props: PropsList) {
    const list_of_opencritic_elements = props.data.map((element) =>
        <li className="py-3 sm:pb-4 cursor-pointer" onClick={() => props.handleNavigation(element.url, "opencritic")}>
                    <div className="flex items-center space-x-4 rtl:space-x-reverse h-14">
                        <div className="flex-shrink-0">
                            {element.img ? <img className="w-14 h-14 rounded-full" src={element.img.src} alt=""/>: <img className="w-14 h-14 rounded-full" src="/no_image.jpg" alt="no_image"/>}
                        </div>
                        <div className="flex-1 min-w-0">
                            <p className="text-sm font-medium text-gray-900 truncate dark:text-white">
                                {element.name}
                            </p>
                        </div>
                        <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">
                            {element.critic_score}
                        </div>
                    </div>
                </li>

    )
    return (
        <>
            <ul
                className="w-4/5 lg:w-2/5 divide-y divide-gray-200 dark:divide-gray-700"
            >
                {list_of_opencritic_elements}
            </ul>
        </>
    )
}

// OpencriticList.propTypes = {
//     handleNavigation: PropTypes.func,
//     data: PropTypes.array
// };
export default OpencriticList;