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
                            <img className="w-14 h-14 rounded-full" src={element.img}
                                 alt=""/>
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
            {/*{list_of_metacritic_elements}*/}

            <ul
                // className="max-w-md divide-y divide-gray-200 dark:divide-gray-700"
                className="divide-y divide-gray-200 dark:divide-gray-700"
            >
                {list_of_metacritic_elements}
                {/*<li className="pb-3 sm:pb-4">*/}
                {/*    <div className="flex items-center space-x-4 rtl:space-x-reverse">*/}
                {/*        <div className="flex-shrink-0">*/}
                {/*            <img className="w-8 h-8 rounded-full" src="/docs/images/people/profile-picture-1.jpg"*/}
                {/*                 alt="Neil image"/>*/}
                {/*        </div>*/}
                {/*        <div className="flex-1 min-w-0">*/}
                {/*            <p className="text-sm font-medium text-gray-900 truncate dark:text-white">*/}
                {/*                Neil Sims*/}
                {/*            </p>*/}
                {/*            <p className="text-sm text-gray-500 truncate dark:text-gray-400">*/}
                {/*                email@flowbite.com*/}
                {/*            </p>*/}
                {/*        </div>*/}
                {/*        <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">*/}
                {/*            $320*/}
                {/*        </div>*/}
                {/*    </div>*/}
                {/*</li>*/}
                {/*<li className="py-3 sm:py-4">*/}
                {/*    <div className="flex items-center space-x-4 rtl:space-x-reverse">*/}
                {/*        <div className="flex-shrink-0">*/}
                {/*            <img className="w-8 h-8 rounded-full" src="/docs/images/people/profile-picture-3.jpg"*/}
                {/*                 alt="Neil image"/>*/}
                {/*        </div>*/}
                {/*        <div className="flex-1 min-w-0">*/}
                {/*            <p className="text-sm font-medium text-gray-900 truncate dark:text-white">*/}
                {/*                Bonnie Green*/}
                {/*            </p>*/}
                {/*            <p className="text-sm text-gray-500 truncate dark:text-gray-400">*/}
                {/*                email@flowbite.com*/}
                {/*            </p>*/}
                {/*        </div>*/}
                {/*        <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">*/}
                {/*            $3467*/}
                {/*        </div>*/}
                {/*    </div>*/}
                {/*</li>*/}
                {/*<li className="py-3 sm:py-4">*/}
                {/*    <div className="flex items-center space-x-4 rtl:space-x-reverse">*/}
                {/*        <div className="flex-shrink-0">*/}
                {/*            <img className="w-8 h-8 rounded-full" src="/docs/images/people/profile-picture-2.jpg"*/}
                {/*                 alt="Neil image"/>*/}
                {/*        </div>*/}
                {/*        <div className="flex-1 min-w-0">*/}
                {/*            <p className="text-sm font-medium text-gray-900 truncate dark:text-white">*/}
                {/*                Michael Gough*/}
                {/*            </p>*/}
                {/*            <p className="text-sm text-gray-500 truncate dark:text-gray-400">*/}
                {/*                email@flowbite.com*/}
                {/*            </p>*/}
                {/*        </div>*/}
                {/*        <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">*/}
                {/*            $67*/}
                {/*        </div>*/}
                {/*    </div>*/}
                {/*</li>*/}
                {/*<li className="py-3 sm:py-4">*/}
                {/*    <div className="flex items-center space-x-4 rtl:space-x-reverse">*/}
                {/*        <div className="flex-shrink-0">*/}
                {/*            <img className="w-8 h-8 rounded-full" src="/docs/images/people/profile-picture-5.jpg"*/}
                {/*                 alt="Neil image"/>*/}
                {/*        </div>*/}
                {/*        <div className="flex-1 min-w-0">*/}
                {/*            <p className="text-sm font-medium text-gray-900 truncate dark:text-white">*/}
                {/*                Thomas Lean*/}
                {/*            </p>*/}
                {/*            <p className="text-sm text-gray-500 truncate dark:text-gray-400">*/}
                {/*                email@flowbite.com*/}
                {/*            </p>*/}
                {/*        </div>*/}
                {/*        <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">*/}
                {/*            $2367*/}
                {/*        </div>*/}
                {/*    </div>*/}
                {/*</li>*/}
                {/*<li className="pt-3 pb-0 sm:pt-4">*/}
                {/*    <div className="flex items-center space-x-4 rtl:space-x-reverse">*/}
                {/*        <div className="flex-shrink-0">*/}
                {/*            <img className="w-8 h-8 rounded-full" src="/docs/images/people/profile-picture-4.jpg"*/}
                {/*                 alt="Neil image"/>*/}
                {/*        </div>*/}
                {/*        <div className="flex-1 min-w-0">*/}
                {/*            <p className="text-sm font-medium text-gray-900 truncate dark:text-white">*/}
                {/*                Lana Byrd*/}
                {/*            </p>*/}
                {/*            <p className="text-sm text-gray-500 truncate dark:text-gray-400">*/}
                {/*                email@flowbite.com*/}
                {/*            </p>*/}
                {/*        </div>*/}
                {/*        <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">*/}
                {/*            $367*/}
                {/*        </div>*/}
                {/*    </div>*/}
                {/*</li>*/}
            </ul>

        </>
    )
};

// MetacriticList.propTypes = {
//     handleNavigation: PropTypes.func,
//     data: PropTypes.array
// };

export default MetacriticList;
