<template>
    <div class="mr-2 mb-[3%] mt-[3%] ml-2 font-serif">
        <div class="fixed top-0 left-0 right-0 bg-white z-10 shadow-md py-4 px-6 flex items-center justify-between">
            <span class="font-bold">
                <h1 class="text-[30px]">
                    Sri Sakthi Tyres
                </h1>
                <h1 class="text-2xl font-semibold">
                    Perundurai Road, Erode,<br>
                    Tamil Nadu.
                </h1>
            </span>
            <div v-if="Auth" class="flex flex-col space-y-1 items-center mr-[50px]">
                <h1 class="text-[20px] font-bold mb-6">Welcome User</h1>
            </div>
        </div>
        <div>
            <div v-if="!selectImg" class="flex justify-center mt-[300px]">
                <div class="flex flex-row space-x-8">
                    <div class="person-container">
                        <img class="w-237 h-188"
                            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0-FVVaYSFbTMXiC6bUW2O_Vzx0OyauBu_RwRlfQ7iIU5aMvWJ86dpdfvGL7eYThBSkQ0&usqp=CAU"
                            alt="person-1" @click="handleImgSelection" />
                        <p>Vignesh</p>
                    </div>
                    <div class="person-container">
                        <img class="w-237 h-188"
                            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0-FVVaYSFbTMXiC6bUW2O_Vzx0OyauBu_RwRlfQ7iIU5aMvWJ86dpdfvGL7eYThBSkQ0&usqp=CAU"
                            alt="person-2" @click="handleImgSelection" />
                        <p>Yesha</p>
                    </div>
                    <div class="person-container">
                        <img class="w-237 h-188"
                            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0-FVVaYSFbTMXiC6bUW2O_Vzx0OyauBu_RwRlfQ7iIU5aMvWJ86dpdfvGL7eYThBSkQ0&usqp=CAU"
                            alt="person-3" @click="handleImgSelection" />
                        <p>Vijay</p>
                    </div>
                    <div class="person-container">
                        <img class="w-237 h-188"
                            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0-FVVaYSFbTMXiC6bUW2O_Vzx0OyauBu_RwRlfQ7iIU5aMvWJ86dpdfvGL7eYThBSkQ0&usqp=CAU"
                            alt="person-4" @click="handleImgSelection" />
                        <p>Kavil</p>
                    </div>
                </div>
            </div>
            <div v-if="selectImg && !Auth" class="flex flex-col space-y-3 justify-center mt-[300px] items-center ">
                <div v-if="incorrect"
                    class="flex items-center p-4 mb-4 text-lg text-red-800 border border-red-300 rounded-lg bg-red-50 dark:bg-white-800 dark:text-red-800 dark:border-red-900"
                    role="alert">
                    <svg class="flex-shrink-0 inline w-5 h-5 me-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor" viewBox="0 0 20 20">
                        <path
                            d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z" />
                    </svg>
                    <span class="sr-only">Info</span>&nbsp;
                    <div>
                        <span class="font-medium">Danger alert!</span> Change a few things up and try submitting again.
                    </div>
                </div>
                <div>
                    <FeatherIcon name="arrow-left" class="w-10 h-10 absolute top-[15%] right-[93%] cursor-pointer"
                        @click="selectImg = false" />
                </div>
                <div class="flex flex-col space-y-7 justify-center items-center p-[60px] rounded-lg"
                    style="box-shadow: 5px 5px 10px rgba(1, 1, 0.5, 0.5); background: linear-gradient(135deg, #7469B6, #AD88C6, #E1AFD1);">
                    <div class="mb-4" style="width: 237.48px; height: 227.17px;">
                        <img style="width: 100%; height: 100%; object-fit: contain;" :src="data.selectedImgSrc"
                            :alt="data.selectedAlt" />
                    </div>
                    <div class="mb-4">
                        <h1 class="text-center text-2xl font-semibold" style="color: #333;">User-1</h1>
                    </div>
                    <div class="mb-4">
                        <h1 class="text-xl font-semibold" style="color: #333;">Enter your 4 Digit Pin</h1>
                    </div>
                    <div class="flex flex-row space-x-8">
                        <input class="w-16 h-16 text-center border-2 border-black-500 bg-gray-200 rounded-lg"
                            type="password" v-model="pin1" maxlength="1" @input="focusNext($event, 1)"
                            style="color: #333;">
                        <input class="w-16 h-16 text-center border-2 border-black-500 bg-gray-200 rounded-lg"
                            type="password" v-model="pin2" maxlength="1" @input="focusNext($event, 2)"
                            style="color: #333;">
                        <input class="w-16 h-16 text-center border-2 border-black-500 bg-gray-200 rounded-lg"
                            type="password" v-model="pin3" maxlength="1" @input="focusNext($event, 3)"
                            style="color: #333;">
                        <input class="w-16 h-16 text-center border-2 border-black-500 bg-gray-200 rounded-lg"
                            type="password" v-model="pin4" maxlength="1" @input="focusNext($event, 4)"
                            style="color: #333;">
                    </div>
                </div>
            </div>
            <!-- main page -->
            <div v-if="currentstep == 0 && Auth">
                <div class="pt-24">
                    <div v-if="currentstep == 0">
                        <div v-if="noData">
                            <div class="flex justify-center">
                                <span class="font-medium text-red-500">No data found!</span>
                            </div>
                        </div>
                        <div v-if="showConfirmation"
                            class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-center items-center">
                            <div class="bg-white rounded-lg p-8 shadow-xl">
                                <h2 class="text-xl font-semibold mb-4">Confirm Save</h2>
                                <p class="mb-4">Are you sure you want to save the details?</p>
                                <div class="flex justify-center">
                                    <button @click="confirmSave" v-if="newVehicleSave"
                                        class="bg-green-500 text-white font-semibold px-4 py-2 rounded mr-2">Save</button>
                                    <button @click="cancelSave"
                                        class="bg-red-500 text-white font-semibold px-4 py-2 rounded">Cancel</button>
                                </div>
                            </div>
                        </div>
                        <div v-if="noMessage"
                            class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-center items-center">
                            <div class="bg-white rounded-lg p-8 shadow-xl">
                                <h2 class="text-xl font-semibold mb-4">Nothing to Show ! 😄</h2>
                            </div>
                        </div>
                        <div v-if="billPopup == 'true'"
                            class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-center items-center">
                            <a href="#"
                                class="block max-w-[70rem] p-10 pt-5 bg-white border border-gray-200 rounded-lg shadow">
                                <div class="grid grid-cols-2">
                                    <div>
                                        <h5 class="mb-2 text-2xl font-bold tracking-tight text-black">
                                            Price Details</h5>
                                    </div>
                                </div>
                                <div class="relative overflow-x-auto">
                                    <table
                                        class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                        <thead
                                            class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                            <tr>
                                                <th scope="col" class="px-6 py-3">
                                                    Items
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Size
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Type
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Pattern
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Rate
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Quantity
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Amount
                                                </th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                                                v-for="(item, index) in popItems.lead_item" :key="index">
                                                <td class="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                                                    scope="row">{{ item.item_code }}</td>
                                                <td class="px-6 py-3">{{ item.size }}</td>
                                                <td class="px-6 py-3">{{ item.tyre_type }}</td>
                                                <td class="px-6 py-3">{{ item.pattern }}</td>
                                                <td class="px-6 py-3">{{ item.rate }}</td>
                                                <td class="px-6 py-3">{{ item.quantity }}</td>
                                                <td class="px-6 py-3">{{ item.amount }}</td>
                                            </tr>
                                            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                                                <td></td>
                                                <td></td>
                                                <td></td>
                                                <td></td>
                                                <td></td>
                                                <td
                                                    class="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                                    Total Amount</td>
                                                <td class="px-6 py-3">{{ popItems.total_amount }}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                                <div class="grid grid-cols-2 gap-10">
                                    <Button class="flex justify-end mt-3" :variant="'solid'" theme="green" size="sm"
                                        @click="enquiryClear">OK</Button>
                                    <Button class="flex justify-end mt-3" :variant="'solid'" theme="red" size="sm"
                                        @click="deleteEnquiry">Cancel</Button>
                                </div>
                            </a>
                        </div>
                        <div v-if="showWarning"
                            class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-center items-center">
                            <div class="bg-white rounded-lg p-8 shadow-xl">
                                <p class="mb-4 font-bold text-red-500">Please fill the required fields!</p>
                            </div>
                        </div>
                        <div v-if="showAlerts"
                            class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-center items-center">
                            <div class="bg-white rounded-lg p-8 shadow-xl">
                                <p class="mb-4 text-red-500 font-bold" v-if="vehicleNumber">Please fill the required
                                    fields!</p>
                                <p class="mb-4 text-red-500 font-bold" v-if="mobileNumber">Customer Mobile Number
                                    already exist!</p>
                                <p class="mb-4 text-red-500 font-bold" v-if="searchValue">Please fill the search value!
                                </p>
                                <p class="mb-4 text-red-500 font-bold" v-if="wrongSearchValue">Enter valid Vehicle
                                    Number!</p>
                                <p class="mb-4 text-red-500 font-bold" v-if="vehicleExist">Vehicle already exists!</p>
                                <p class="mb-4 text-green-500 font-bold" v-if="successData">Details added successfully!
                                </p>
                                <p class="mb-4 text-green-500 font-bold" v-if="modifyAlert">Successfully modified
                                    vehicle data!
                                </p>
                                <p class="mb-4 text-red-500 font-bold" v-if="notVehicleAlert">Vehicle not exists!</p>
                                <p class="mb-4 text-red-500 font-bold" v-if="noVehicleNumber">Enter vehicle number!</p>
                                <p class="mb-4 text-red-500 font-bold" v-if="noValidVehicleNumber">Enter valid vehicle
                                    number!</p>
                                <p class="mb-4 text-red-500 font-bold" v-if="noCustomerValidVehicleNumber">Enter valid
                                    vehicle number!</p>
                                <p class="mb-4 text-red-500 font-bold" v-if="notCustomerAlert">Please fill the Customer
                                    details!</p>
                                <p class="mb-4 text-red-500 font-bold" v-if="notEmployeeAlert">Please add atleast one
                                    Employee!</p>
                                <p class="mb-4 text-red-500 font-bold" v-if="notEmpDetailAlert">Please fill required
                                    Employee details!</p>
                                <p class="mb-4 text-green-500 font-bold" v-if="deleteConfirmation">Vehicle details
                                    deleted
                                    successfully!</p>
                                <p class="mb-4 text-red-500 font-bold" v-if="cannotSave">! It's a search details. Can't
                                    save..</p>
                                <p class="mb-4 text-red-500 font-bold" v-if="customerExist">! Customer already added to
                                    this
                                    vehicle..</p>
                                <p class="mb-4 text-red-500 font-bold" v-if="leadMobile">Lead Customer not found!</p>
                                <p class="mb-4 text-red-500 font-bold" v-if="leadCustomer">Lead Customer already exists!
                                </p>
                            </div>
                        </div>
                        <div v-if="showDeleteConfirmation"
                            class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-center items-center">
                            <div class="bg-white rounded-lg p-8 shadow-xl">
                                <h2 class="text-xl font-semibold mb-4">Confirm Delete</h2>
                                <p class="mb-4">Are you sure want to delete the details?</p>
                                <div class="flex justify-center">
                                    <button
                                        @click="confirmDelete(responseData && responseData.message && responseData.message[0]?.name)"
                                        class="bg-red-500 text-white font-semibold px-4 py-2 rounded mr-2">Delete</button>
                                    <button @click="cancelDelete"
                                        class="bg-gray-500 text-white font-semibold px-4 py-2 rounded">Cancel</button>
                                </div>
                            </div>
                        </div>
                        <div v-if="hide == 'false' && hideEnq == 'false'" class="relative cursor-pointer ml-1">
                            <div class="flex justify-between items-center  text-black p-3 mt-1 rounded-lg w-15"
                                @click="toggleMenu">
                                <FeatherIcon name="menu" width="35" height="35"></FeatherIcon>
                            </div>
                            <div v-if="showMenu"
                                class="absolute left-0 mt-1 border border-gray-300 ml-3 bg-white rounded-lg shadow-lg w-40">
                                <div class="px-4 py-2 hover:bg-gray-100 cursor-pointer"
                                    @click="getJobCard(), showMenu = false">
                                    <button v-if="hide == 'false' && hideEnq == 'false'">Job Card List</button>
                                </div>
                                <div class="px-4 py-2 hover:bg-gray-100 cursor-pointer"
                                    @click="getEnquiry(), showMenu = false">
                                    <button v-if="hideEnq == 'false' && hide == 'false'">Enquiry</button>
                                </div>
                                <div class="px-4 py-2 hover:bg-gray-100 cursor-pointer"
                                    @click="currentstep = 4; billing = true; showMenu = false">
                                    <button v-if="hideEnq == 'false' && hide == 'false'">Billing</button>
                                </div>
                            </div>
                        </div>

                        <div class="flex justify-center m-5" v-if="searchShow">
                            <div class="flex items-center space-x-3">
                                <input type="text"
                                    class="w-[338px] h-[52px] rounded-sm border-solid border border-black"
                                    v-model="searchQuery" @keyup.enter="search" placeholder="Enter Vehicle Number">
                                <button class="bg-blue-500 w-[150px] text-white font-bold text-base p-4 rounded-lg"
                                    @click="search">Search</button>
                            </div>
                        </div>
                        <div v-if="(hasResponse && initial) || checked">
                            <div class="flex ml-6">
                                <div class="mr-8">
                                    <!-- <button @click="getJobCard" v-if="hide == 'false' && hideEnq == 'false'"
                                        class="bg-blue-500 w-[100px] text-white font-bold p-2 rounded-lg mt-4 mb-4">Job
                                        Card</button> -->
                                    <button
                                        @click="hide = 'false', check = 'false', initial = 'true', initialNext = (responseData && responseData.message && nextButtonEnable) ? 'true' : 'false', searchShow = 'true', jobCardPopup = 'false'"
                                        v-if="hide != 'false'"
                                        class="bg-blue-500 w-[100px] text-white font-bold p-2 rounded-lg mt-4 mb-4">Back</button>
                                </div>
                                <div>
                                    <!-- <button @click="getEnquiry" v-if="hideEnq == 'false' && hide == 'false'"
                                        class="bg-blue-500 w-[100px] text-white font-bold p-2 rounded-lg mt-4 mb-4">Enquiry</button> -->
                                    <button
                                        @click="hideEnq = 'false', check = 'false', initial = 'true', initialNext = (responseData && responseData.message && nextButtonEnable) ? 'true' : 'false', searchShow = 'true', enquiryPopup = 'false'"
                                        v-if="hideEnq != 'false'"
                                        class="bg-blue-500 w-[100px] text-white font-bold p-2 rounded-lg mt-4 mb-4">Back</button>
                                </div>
                                <!-- <div class="ml-6">
                                    <button @click="currentstep = 4; billing = true" v-if="hideEnq == 'false' && hide == 'false'"
                                        class="bg-blue-500 w-[100px] text-white font-bold p-2 rounded-lg mt-4 mb-4">Billing</button>
                                </div> -->
                                <div>
                                    <input type="number" placeholder="search ..." v-if="hideEnq != 'false'"
                                        v-model="searchEnquiry"
                                        class="mt-20 mb-5 ml-[-6.2rem] p-4 w-[200px] h-[40px] rounded-sm border-solid border border-black" />
                                    <input placeholder="Vehicle Search ..."
                                        v-if="hide != 'false' && jobCardPopup == 'false'" v-model="searchJobCard"
                                        class="mt-20 mb-5 ml-[-6.2rem] p-4 w-[200px] h-[40px] rounded-sm border-solid border border-black" />
                                </div>
                            </div>
                            <div v-if="jobCardPopup == 'false'">
                                <div class="relative overflow-x-auto flex justify-center" v-if="hide != 'false'">
                                    <table
                                        class="w-[75rem] text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                        <thead
                                            class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                            <tr>
                                                <th scope="col" class="px-6 py-3">
                                                    ID
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Time_in
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Vehicle No
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Owner
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Mobile Number
                                                </th>
                                            </tr>
                                        </thead>
                                        <tbody style="max-height: 2rem; overflow-y: auto;">
                                            <tr class="bg-white border-b dark:border-gray-700 dark:text-black"
                                                @click="fetchJobCard(jobcard.name)" v-for="jobcard in jobCardDetails"
                                                :key="jobcard">
                                                <th scope="row"
                                                    class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-black">
                                                    <a href="#">{{ jobcard.name
                                                        }}</a>
                                                </th>
                                                <td class="px-6 py-4">
                                                    {{ jobcard.time_in }}
                                                </td>
                                                <td class="px-6 py-4">
                                                    {{ jobcard.vehicle_no }}
                                                </td>
                                                <td class="px-6 py-4">
                                                    {{ jobcard.customer }}
                                                </td>
                                                <td class="px-6 py-4">
                                                    {{ jobcard.mobile_no }}
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            <div v-if="jobCardPopup == 'true'" class="relative overflow-x-auto flex justify-center">
                                <a href="#"
                                    class="block max-w-[70rem] p-10 pt-5 bg-white border border-gray-200 rounded-lg shadow">
                                    <div class="grid grid-cols-2">
                                        <div>
                                            <h5 class="mb-2 text-2xl font-bold tracking-tight text-black">
                                                Details</h5>
                                        </div>
                                        <div class="flex justify-end">
                                            <button @click="jobCardPopup = 'false'">
                                                <svg class="w-3 h-3" aria-hidden="true"
                                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                                                    <path stroke="currentColor" stroke-linecap="round"
                                                        stroke-linejoin="round" stroke-width="2"
                                                        d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                                                </svg>
                                            </button>
                                        </div>
                                    </div>
                                    <div class="relative overflow-x-auto">
                                        <table
                                            class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                            <thead
                                                class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                                <tr>
                                                    <th scope="col" class="px-6 py-3">
                                                        Item Code
                                                    </th>
                                                    <th scope="col" class="px-6 py-3">
                                                        Warehouse
                                                    </th>
                                                    <th scope="col" class="px-6 py-3">
                                                        Warranty
                                                    </th>
                                                    <th scope="col" class="px-6 py-3">
                                                        Warranty Expired
                                                    </th>
                                                    <th scope="col" class="px-6 py-3">
                                                        Quantity
                                                    </th>
                                                    <th scope="col" class="px-6 py-3">
                                                        Rate
                                                    </th>
                                                    <th scope="col" class="px-6 py-3">
                                                        Amount
                                                    </th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                                                    v-for="(item, index) in jobCardData.billing_details" :key="index">
                                                    <td class="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                                                        scope="row">{{ item.item_code + additional(item.additional) }}
                                                    </td>
                                                    <td class="px-6 py-3">{{ item.warehouse }}</td>
                                                    <td class="px-6 py-3">{{ formatValue(item.warranty, 'warranty') }}
                                                    </td>
                                                    <td class="px-6 py-3">{{ formatValue(item.max_years, 'years') }}
                                                    </td>
                                                    <td class="px-6 py-3">{{ item.quantity }}</td>
                                                    <td class="px-6 py-3">{{ item.rate }}</td>
                                                    <td class="px-6 py-3">{{ item.amount }}</td>
                                                </tr>
                                                <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                                                    <td colspan="4"></td>
                                                    <td colspan="2"
                                                        class="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white text-center">
                                                        Total Amount</td>
                                                    <td class="px-6 py-3">{{ jobCardData.total_amount }}</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </a>
                            </div>
                            <div v-if="enquiryPopup == 'false'">
                                <div class="relative overflow-x-auto flex justify-center" v-if="hideEnq != 'false'">
                                    <div>
                                        <table
                                            class="w-[75rem] text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                            <thead
                                                class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                                <tr>
                                                    <th scope="col" class="px-6 py-3">
                                                        ID
                                                    </th>
                                                    <th scope="col" class="px-6 py-3">
                                                        Name
                                                    </th>
                                                    <th scope="col" class="px-6 py-3">
                                                        Mobile Number
                                                    </th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr class="bg-white border-b  dark:border-gray-700 dark:text-black"
                                                    @click="fetchEnquiry(enquiry.name)"
                                                    v-for="enquiry in enquiryDetails" :key="enquiry">
                                                    <th scope="row"
                                                        class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-black">
                                                        {{ enquiry.name }}
                                                    </th>
                                                    <td class="px-6 py-4">
                                                        {{ enquiry.lead_name }}
                                                    </td>
                                                    <td class="px-6 py-4">
                                                        {{ enquiry.mobile_no }}
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                            <div v-if="enquiryPopup == 'true'" class="relative overflow-x-auto flex justify-center">
                                <a href="#"
                                    class="block max-w-[70rem] p-10 pt-5 bg-white border border-gray-200 rounded-lg shadow">
                                    <div class="grid grid-cols-2">
                                        <div>
                                            <h5 class="mb-2 text-2xl font-bold tracking-tight text-black">
                                                Details</h5>
                                        </div>
                                        <div class="flex justify-end">
                                            <button @click="enquiryPopup = 'false'">
                                                <svg class="w-3 h-3" aria-hidden="true"
                                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                                                    <path stroke="currentColor" stroke-linecap="round"
                                                        stroke-linejoin="round" stroke-width="2"
                                                        d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                                                </svg>
                                            </button>
                                        </div>
                                    </div>
                                    <div class="relative overflow-x-auto">
                                        <table
                                            class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                            <thead
                                                class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                                <tr>
                                                    <th scope="col" class="px-6 py-3">
                                                        Item Code
                                                    </th>
                                                    <th scope="col" class="px-6 py-3">
                                                        Brand
                                                    </th>
                                                    <th scope="col" class="px-6 py-3">
                                                        Quantity
                                                    </th>
                                                    <th scope="col" class="px-6 py-3">
                                                        Rate
                                                    </th>
                                                    <th scope="col" class="px-6 py-3">
                                                        Amount
                                                    </th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                                                    v-for="(item, index) in enquiryData.enquiry_details" :key="index">
                                                    <td class="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                                                        scope="row">{{
                                                            item.item_code }}</td>
                                                    <td class="px-6 py-3">{{ item.brand }}</td>
                                                    <td class="px-6 py-3">{{ item.quantity }}</td>
                                                    <td class="px-6 py-3">{{ item.rate }}</td>
                                                    <td class="px-6 py-3">{{ item.amount }}</td>
                                                </tr>
                                                <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                                                    <td></td>
                                                    <td></td>
                                                    <td></td>
                                                    <td
                                                        class="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                                        Total Amount</td>
                                                    <td class="px-6 py-3">{{ enquiryData.total_amount }}</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </a>
                            </div>
                            <div v-if="hasResponse && initial">
                                <div class="flex justify-center" v-if="hide == 'false' && hideEnq == 'false'">
                                    <div class="flex justify-center mt-9">
                                        <img src="https://img.freepik.com/free-vector/hand-drawn-no-data-concept_52683-127823.jpg?w=996&t=st=1712321166~exp=1712321766~hmac=ae2f4e19eb0e1185d52ac8a07c158e9dc5afa741284e9526a8e8a0165573735b"
                                            alt="No data" class="w-[25%]" @click="showMessage">
                                    </div>
                                </div>
                                <div class="flex justify-center m-5" v-if="hide == 'false' && hideEnq == 'false'">
                                    <button class="bg-blue-500 w-[150px] text-white font-bold  p-4 rounded-lg ml-3"
                                        @click="addVehicle">
                                        Add Vehicle
                                    </button>
                                    <button class="bg-blue-500 w-[150px] text-white font-bold  p-4 rounded-lg ml-3"
                                        @click="addCustomer" id="customerId">
                                        Add Customer
                                    </button>

                                </div>
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3" v-if="(responseData && responseData.message && check)">
                            <Card class="bg-gray-200">
                                <div>
                                    <h4 class="text-[20px] font-bold">Vehicle Details</h4>
                                    <hr class="dark-hr">
                                    <div class="grid grid-cols-2">
                                        <div>
                                            <div class="mt-2">
                                                <label>Vehicle Number&emsp;&nbsp;:&nbsp;</label>
                                                <label>
                                                    {{ responseData && responseData.message &&
                                                        responseData.message[0]?.name || 'No data' }}
                                                </label>
                                            </div>
                                            <div class="mt-2">
                                                <label>Vehicle Brand&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;</label>
                                                <label class="mt-3"> {{
                                                    responseData && responseData.message &&
                                                    responseData.message[0]?.vehicle_brand || 'No data' }}</label>
                                            </div>
                                            <div class="mt-2">
                                                <label>Fuel
                                                    Type&nbsp;&nbsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;:&nbsp;</label>
                                                <label class="mt-3"> {{ responseData && responseData.message &&
                                                    responseData.message[0]?.fuel_type
                                                    || 'No data'
                                                    }}</label>
                                            </div>
                                            <div class="mt-2">
                                                <label>Tyre Change(kms)&nbsp;:&nbsp;</label>
                                                <label class="mt-3">{{ responseData && responseData.message &&
                                                    responseData.message[0]?.tyre_change
                                                    || 'No data'
                                                    }}</label>
                                            </div>
                                        </div>
                                        <div>
                                            <div class="mt-2">
                                                <label>Vehicle Model&nbsp;&nbsp;: </label>
                                                <label class="mt-3">
                                                    {{ responseData && responseData.message &&
                                                        responseData.message[0]?.vehicle_model || 'No data' }}</label>
                                            </div>
                                            <div class="mt-2">
                                                <label>Odometer reading&nbsp;&nbsp;:&nbsp;</label>
                                                <label class="mt-3">
                                                    {{ responseData && responseData.message &&
                                                        responseData.message[0]?.last_odometer_reading
                                                        || 'No data' }}</label>
                                            </div>
                                            <div class="mt-2">
                                                <label>Alignment (kms)&nbsp;&nbsp;:&nbsp;</label>
                                                <label class="mt-3"> {{ responseData && responseData.message &&
                                                    responseData.message[0]?.alignment
                                                    || 'No data'
                                                    }}</label>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="mt-[70px] flex flex-row space-x-9">
                                        <button class="bg-blue-500 w-[150px] text-white font-bold  p-4 rounded-lg ml-3"
                                            @click="addVehicle">
                                            Add Vehicle
                                        </button>
                                        <button class="bg-blue-500 w-[150px] text-white font-bold  p-4 rounded-lg ml-3"
                                            @click="modifyVehicle">Modify</button>
                                    </div>
                                </div>
                            </Card>
                            <Card class="bg-gray-200">
                                <div>
                                    <h4 class="text-[20px] font-bold">Customer Details</h4>
                                    <hr class="dark-hr">
                                    <div class="grid grid-cols-2 pl-1">
                                        <div>
                                            <div class="mt-2">
                                                <label>Customer Name&nbsp;&nbsp;:&nbsp; </label>
                                                <label class="mt-3">
                                                    {{ responseData && responseData.message &&
                                                        responseData.message[1]?.current_owner || 'No data' }}
                                                </label>
                                                <br>
                                                <input type="checkbox"
                                                    :checked="responseData && responseData.message && responseData.message[1].whatsapp === 1"
                                                    :disabled="!isEditMode"
                                                    @change="responseData && responseData.message && (responseData.message[1].whatsapp = $event.target.checked ? 1 : 0)"
                                                    class="bg-gray-300 rounded-sm">
                                                &nbsp;&nbsp;<label>WhatsApp</label>
                                                <span class="ml-5">
                                                    <input type="checkbox"
                                                        :checked="responseData && responseData.message && responseData.message[1].call === 1"
                                                        :disabled="!isEditMode"
                                                        @change="responseData && responseData.message && (responseData.message[1].call = $event.target.checked ? 1 : 0)"
                                                        class="bg-gray-300 rounded-sm">
                                                    &nbsp;&nbsp;<label>Call</label>
                                                </span>
                                            </div>
                                            <div class="mt-2">
                                                <label>Driver Name&nbsp;&nbsp;:&nbsp;</label>
                                                <label class="mt-3">
                                                    {{ responseData &&

                                                        responseData.message && responseData.message[2][0]?.full_name ||
                                                        'No data' }}

                                                </label>
                                                <br>
                                                <input type="checkbox"
                                                    :checked="responseData && responseData.message && responseData.message[2] && responseData.message[2][0]?.custom_whatsapp_check === 1"
                                                    :disabled="!isEditMode"
                                                    @change="responseData && responseData.message && (responseData.message[2][0].custom_whatsapp_check = $event.target.checked ? 1 : 0)"
                                                    class="bg-gray-300 rounded-sm">
                                                &nbsp;&nbsp;<label>WhatsApp</label>
                                                <span class="ml-5">
                                                    <input type="checkbox"
                                                        :checked="responseData && responseData.message && responseData.message[2] && responseData.message[2][0]?.custom_call_check === 1"
                                                        :disabled="!isEditMode"
                                                        @change="responseData && responseData.message && (responseData.message[2][0].custom_call_check = $event.target.checked ? 1 : 0)"
                                                        class="bg-gray-300 rounded-sm">
                                                    &nbsp;&nbsp;<label>Call</label>
                                                </span>
                                            </div>
                                            <div class="mt-2">
                                                <label>Contact Person&nbsp;&nbsp;:&nbsp;</label>
                                                <label class="mt-3">
                                                    {{ responseData && responseData.message &&
                                                        responseData.message[2][1]?.contact_person_name || 'No data' }}
                                                </label>
                                                <br>
                                                <input type="checkbox"
                                                    :checked="responseData && responseData.message && responseData.message[2] && responseData.message[2][1]?.whatsapp === 1"
                                                    :disabled="!isEditMode"
                                                    @change="responseData && responseData.message && (responseData.message[2][1].whatsapp = $event.target.checked ? 1 : 0)"
                                                    class="bg-gray-300 rounded-sm">
                                                &nbsp;&nbsp;<label>WhatsApp</label>
                                                <span class="ml-5">
                                                    <input type="checkbox"
                                                        :checked="responseData && responseData.message && responseData.message[2] && responseData.message[2][1]?.call === 1"
                                                        :disabled="!isEditMode"
                                                        @change="responseData && responseData.message && (responseData.message[2][1].call = $event.target.checked ? 1 : 0)"
                                                        class="bg-gray-300 rounded-sm">
                                                    &nbsp;&nbsp;<label>Call</label>
                                                </span>
                                            </div>
                                        </div>
                                        <div>
                                            <div class="mt-2">
                                                <label>Customer Mobile&nbsp;&nbsp;:&nbsp;</label>
                                                <label class="mt-3">
                                                    {{ responseData && responseData.message &&
                                                        responseData.message[1]?.owner_mobile_no || 'No data' }}
                                                </label>
                                                <br>
                                                <span class="ml-5">
                                                    <input type="checkbox"
                                                        :checked="responseData && responseData.message && responseData.message[1].sms === 1"
                                                        :disabled="!isEditMode"
                                                        @change="responseData && responseData.message && (responseData.message[1].sms = $event.target.checked ? 1 : 0)"
                                                        class="bg-gray-300 rounded-sm">
                                                    &nbsp;&nbsp;<label>SMS</label>
                                                </span>
                                            </div>
                                            <div class="mt-2">
                                                <label>Driver Mobile&nbsp;&nbsp;:&nbsp;</label>
                                                <label class="mt-3">
                                                    {{ responseData && responseData.message &&
                                                        responseData.message[2][0]?.cell_number
                                                        || 'No data' }}
                                                </label>
                                                <br>
                                                <span class="ml-5">
                                                    <input type="checkbox"
                                                        :checked="responseData && responseData.message && responseData.message[2] && responseData.message[2][0]?.custom_sms_check === 1"
                                                        :disabled="!isEditMode"
                                                        @change="responseData && responseData.message && (responseData.message[2][0].custom_sms_check = $event.target.checked ? 1 : 0)"
                                                        class="bg-gray-300 rounded-sm">
                                                    &nbsp;&nbsp;<label>SMS</label>
                                                </span>
                                            </div>
                                            <div class="mt-2">
                                                <label>Contact Person&nbsp;&nbsp;:&nbsp; </label>
                                                <label class="mt-3">
                                                    {{ responseData && responseData.message &&
                                                        responseData.message[2][1]?.contact_person_mobile
                                                        || 'No data' }}
                                                </label>
                                                <br>
                                                <span class="ml-5">
                                                    <input type="checkbox"
                                                        :checked="responseData && responseData.message && responseData.message[2] && responseData.message[2][1]?.sms === 1"
                                                        :disabled="!isEditMode"
                                                        @change="responseData && responseData.message && (responseData.message[2][1].sms = $event.target.checked ? 1 : 0)"
                                                        class="bg-gray-300 rounded-sm">
                                                    &nbsp;&nbsp;<label>SMS</label>
                                                </span>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="float-right mt-[20px] flex flex-row space-x-9">
                                        <button class="bg-blue-500 w-[150px] text-white font-bold  p-4 rounded-lg ml-3"
                                            @click="addCustomer" id="customerId">
                                            Add Customer
                                        </button>
                                        <button class="bg-blue-500 w-[150px] text-white font-bold  p-4 rounded-lg ml-3"
                                            @click="modifyCustomer">Modify</button>
                                    </div>
                                </div>
                            </Card>
                            <div class="mt-3">
                                <button class="bg-red-500 w-[150px] text-white font-bold  p-4 rounded-lg ml-3"
                                    @click="deleteVehicle">Delete</button>
                            </div>
                        </div>
                        <div v-if="showNewVehicle"
                            class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-end items-center pb-10">
                            <div class="fixed inset-0" @click="addVehicle"></div>
                            <div class="max-w-md w-full bg-white shadow-xl h-full overflow-y-auto relative">
                                <button class="absolute to text-black pt-5 font-bold p-2 right-2  px-2 py-1 rounded"
                                    @click="addVehicle">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M6 18L18 6M6 6l12 12" />
                                    </svg>
                                </button>
                                <div class="p-8 mt-[140px]  ">
                                    <h2 class="text-2xl font-semibold mb-4 ">Vehicle Details</h2>
                                    <hr class="dark-hr">
                                    <p class="m-2">Vehicle Number <span class="text-red-500 font-bold">*</span><br>
                                        <input type="text"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.name" placeholder="Enter Vehicle Number">
                                    </p>
                                    <p class="m-2">Vehicle Brand <span class="text-red-500 font-bold">*</span><br>
                                        <select
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.vehicle_brand"
                                            @change="get_Vmodel(vehicleData.vehicle_brand)" style="overflow-y: auto;">
                                            <!-- Loop through vBrand and create an option for each brand -->
                                            <option value="" disabled selected>Select brand...</option>
                                            <option v-for="brand in vBrand" :key="brand">{{ brand.name }}</option>
                                        </select>

                                    </p>
                                    <p class="m-2">Vehicle Model <span class="text-red-500 font-bold">*</span><br>
                                        <select
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.vehicle_model" style="overflow-y: auto;">
                                            <!-- Loop through vBrand and create an option for each brand -->
                                            <option value="" disabled selected>Select model...</option>
                                            <option v-for="model in vModel" :key="model">{{ model.model }}</option>
                                        </select>
                                    </p>
                                    <p class="m-2">Fuel Type <span class="text-red-500 font-bold">*</span><br>
                                        <select v-model="vehicleData.fuel_type"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black">
                                            <option value="" disabled selected>Select fuel type...</option>
                                            <option value="Petrol">Petrol</option>
                                            <option value="Diesel">Diesel</option>
                                            <option value="EV">EV</option>
                                        </select>
                                    </p>
                                    <p class="m-2">Odometer reading (kms) <span
                                            class="text-red-500 font-bold">*</span><br>
                                        <input type="number"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.last_odometer_reading"
                                            placeholder="Enter Odometer reading">
                                    </p>
                                    <p class="m-2">Tyre Change (kms) <span class="text-red-500 font-bold">*</span><br>
                                        <input type="number"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.tyre_change" placeholder="Enter Tyre Change">
                                    </p>
                                    <p class="m-2">Alignment (kms) <span class="text-red-500 font-bold">*</span><br>
                                        <input type="number"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.alignment" placeholder="Enter Alignment">
                                    </p>
                                    <div class="m-3 mt-4 flex flex-row space-x-[70px]">
                                        <button class="bg-green-500 w-[100px] text-white font-bold 0 p-2 rounded"
                                            @click="addVehicleData" @keyup.enter="addVehicleData">Add</button>
                                        <button class="bg-red-500 w-[100px] text-white font-bold ml-3 p-2 rounded"
                                            @click="clearVehicleData">Clear</button>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div v-if="showModifyVehicle"
                            class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-end items-center pb-10">
                            <div class="fixed inset-0" @click="modifyVehicle"></div>
                            <div class="max-w-md w-full bg-white shadow-xl h-full overflow-y-auto relative">
                                <button class="absolute to text-black pt-5 font-bold p-2 right-2 px-2 py-1 rounded"
                                    @click="modifyVehicle">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M6 18L18 6M6 6l12 12" />
                                    </svg>
                                </button>
                                <div class="p-8 mt-[140px]">
                                    <h2 class="text-2xl font-semibold mb-4">Vehicle Details</h2>
                                    <hr class="dark-hr">
                                    <p class="m-2">Vehicle Number <br>
                                        <input type="text" v-if="check"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="responseData.message[0].name"
                                            placeholder="Enter your Vehicle Number">
                                    </p>
                                    <p class="m-2">Vehicle Brand <br>
                                        <select
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="responseData.message[0].vehicle_brand"
                                            @change="get_Vmodel(vehicleData.vehicle_brand)" style="overflow-y: auto;">
                                            <!-- Loop through vBrand and create an option for each brand -->
                                            <option value="" disabled selected>Select brand...</option>
                                            <option v-for="brand in vBrand" :key="brand">{{ brand.name }}</option>
                                        </select>

                                    </p>
                                    <p class="m-2">Vehicle Model <br>
                                        <select
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.vehicle_model" style="overflow-y: auto;">
                                            <!-- Loop through vBrand and create an option for each brand -->
                                            <option value="" disabled selected>Select model...</option>
                                            <option v-for="model in vModel" :key="model">{{ model.model }}</option>
                                        </select>
                                    </p>
                                    <p class="m-2">Fuel Type <br>
                                        <select v-if="check" v-model="responseData.message[0].fuel_type"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black">
                                            <option value="Petrol">Petrol</option>
                                            <option value="Diesel">Diesel</option>
                                            <option value="EV">Electical Vehicle</option>
                                        </select>
                                    </p>
                                    <p class="m-2">Odometer reading <br>
                                        <input type="number" v-if="check"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="responseData.message[0].last_odometer_reading"
                                            placeholder="Enter Odometer reading">
                                    </p>
                                    <p class="m-2">Tyre Change (kms) <br>
                                        <input type="number" v-if="check"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="responseData.message[0].tyre_change"
                                            placeholder="Enter Tyre Change">
                                    </p>
                                    <p class="m-2">Alignment (kms) <br>
                                        <input type="number" v-if="check"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="responseData.message[0].alignment" placeholder="Enter Alignment">
                                    </p>
                                    <div class="m-3 mt-4 flex flex-row space-x-[70px]">
                                        <button class="bg-green-500 w-[100px] text-white font-bold 0 p-2 rounded"
                                            @click="addModifiedData">Save</button>
                                        <button class="bg-red-500 w-[100px] text-white font-bold ml-3 p-2 rounded"
                                            @click="clearModifiedVehicleData">Clear</button>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div v-if="showNewCustomer"
                            class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-end items-center pb-9">
                            <div class="fixed inset-0" @click="addCustomer"></div>
                            <div class="max-w-xl w-full bg-white shadow-xl h-full overflow-y-auto relative">
                                <button class="absolute to text-gray pt-5 font-bold p-2 right-2 px-2 py-1 rounded"
                                    @click="addCustomer">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M6 18L18 6M6 6l12 12" />
                                    </svg>
                                </button>
                                <div class="p-8 mt-[110px]">
                                    <div class="pb-4 grid grid-cols-2 ml-24" v-if="searchMobileAfterResponse">
                                        <input type="tel" v-model="searchMobile"
                                            class="w-[19rem] h-[3rem] mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter Customer Mobile No." @keyup.enter="handleSearch">
                                        <div class="w-[3rem] h-[3rem] mt-1 ml-[7.6rem] bg-blue-600 rounded-sm">
                                            <FeatherIcon name="search" class="m-2 w-8 h-8 cursor-pointer text-gray-100"
                                                @click="handleSearch" />
                                        </div>
                                    </div>
                                    <div class="grid grid-cols-2 mt-[1.5rem]">
                                        <div>
                                            <h2 class="text-2xl font-semibold mb-4">Customer Details</h2>
                                        </div>
                                        <span class="ml-[9rem]" v-if="afterResponse || handle">
                                            <input type="checkbox" v-model="handle" @click="handleEnquiry"
                                                class="bg-gray-300 rounded-sm pb-4">&nbsp;&nbsp;<label>Enquiry</label>
                                        </span>
                                    </div>
                                    <hr class="dark-hr">
                                    <p class="m-2" v-if="!handle && !hasResponse">Vehicle Number <span
                                            class="text-red-500 font-bold">*</span><br>
                                        <input type="text" v-model="responseData.message[0].name" disabled
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter Vehicle Number">
                                    </p>
                                    <p class="m-2">Customer Name <span class="text-red-500 font-bold">*</span><br>
                                        <input type="text" v-model="leadDetails.lead_name" v-if="boolDetails.state == 1"
                                            :readonly="boolDetails.state == 1"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter Name">

                                        <input type="text" v-model="customerData.current_owner"
                                            v-if="boolDetails.state == 0"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter Name">
                                    </p>
                                    <p class="m-2">Customer Mobile No <span class="text-red-500 font-bold">*</span><br>
                                        <input type="tel" v-model="leadDetails.mobile_no" v-if="boolDetails.state == 1"
                                            :readonly="boolDetails.state == 1"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter Mobile No.">

                                        <input type="tel" v-model="customerData.owner_mobile_no"
                                            v-if="boolDetails.state == 0"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter Mobile No.">
                                    </p>
                                    <!-- <p class="m-2">Vehicle Brand <span class="text-red-500 font-bold">*</span><br>
                                        <select
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="customerData.vehicle_brand"
                                            @change="get_Vmodel(vehicleData.vehicle_brand)" style="overflow-y: auto;">
                                            <option value="" disabled selected>Select brand...</option>
                                            <option v-for="brand in vBrand" :key="brand">{{ brand.name }}</option>
                                        </select>
                                    </p>
                                    <p class="m-2">Vehicle Model <span class="text-red-500 font-bold">*</span><br>
                                        <select
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="customerData.vehicle_model" style="overflow-y: auto;">
                                            <option value="" disabled selected>Select model...</option>
                                            <option v-for="model in vModel" :key="model">{{ model.model }}</option>
                                        </select>
                                    </p> -->
                                    <input type="checkbox" v-model="customerData.whatsappChecked"
                                        :checked="leadDetails.custom_whatsapp == '1'" :disabled="boolDetails.state == 1"
                                        class="bg-gray-300 rounded-sm">&nbsp;&nbsp; <label>WhatsApp</label>
                                    <span class="ml-5">
                                        <input type="checkbox" v-model="customerData.callChecked"
                                            :checked="leadDetails.custom_call == '1'" :disabled="boolDetails.state == 1"
                                            class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>call</label>
                                    </span>
                                    <span class="ml-5">
                                        <input type="checkbox" v-model="customerData.smsChecked"
                                            :checked="leadDetails.custom_sms == '1'" :disabled="boolDetails.state == 1"
                                            class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>SMS</label>
                                    </span>

                                    <div v-if="!handle && !hasResponse">

                                        <div v-for="(employee, index) in employees" :key="index" class="mt-2">
                                            <!-- <div v-show="false">{{ sample22 = index }}</div> -->
                                            <hr class="dark-hr m-4">
                                            <button
                                                class="bg-blue-500 w-[100px] text-white font-bold  text-base p-4 rounded-lg mb-1 float-right"
                                                @click="removeEmployee1(index)">Remove</button> <br>
                                            <p class="m-2">Employee Name <span class="text-red-500 font-bold">*</span>
                                                <br>
                                                <input type="text" v-model="employee.driver_name"
                                                    class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                                    placeholder="Enter Name">
                                            </p>
                                            <p class="m-2">Employee Type <span
                                                    class="text-red-500 font-bold">*</span><br>
                                                <select v-model="employee.type" @change="setPrimary(index)"
                                                    class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black">
                                                    <option value="" selected disabled>Please select..</option>
                                                    <option value="current_driver">Driver</option>
                                                    <option value="contact_person">Contact Person</option>
                                                </select>
                                            </p>
                                            <p class="m-2">Phone <span class="text-red-500 font-bold">*</span><br>
                                                <input type="tel" v-model="employee.mobile_no"
                                                    class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                                    placeholder="Enter Mobile No.">
                                            </p>
                                            <input type="checkbox" v-model="employee.whatsappChecked1"
                                                class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>WhatsApp</label>
                                            <span class="ml-5">
                                                <input type="checkbox" v-model="employee.callChecked1"
                                                    class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>Call</label>
                                            </span>
                                            <span class="ml-5">
                                                <input type="checkbox" v-model="employee.smsChecked1"
                                                    class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>SMS</label>
                                            </span>
                                            <span class="ml-5">
                                                <input type="checkbox" v-model="employee.primary"
                                                    @click="handlePrimaryCheckbox(employee)"
                                                    class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>Primary</label>
                                            </span>
                                        </div>
                                        <div>
                                            <button
                                                class="bg-blue-500 w-[100px] text-white font-bold  text-base p-4 rounded-lg mb-1 float-right"
                                                @click="moreEmployee">Add
                                            </button><br>
                                        </div>
                                        <div class="m-3 mt-[40px] flex flex-row space-x-[70px]">
                                            <button
                                                class="bg-green-500 w-[100px]  text-white font-bold 0 text-base p-4 rounded-lg ml-3"
                                                @click="addCustomerData">Save</button>
                                            <button
                                                class="bg-red-500 w-[100px]  text-white font-bold text-base p-4 rounded-lg ml-3"
                                                @click="removeCustomerData">Clear</button>
                                        </div>
                                    </div>
                                    <div v-if="enquiryPage">
                                        <label class="font-semibold">Tyre</label>
                                        <hr class="dark-hr">
                                        <div class="grid grid-cols-4 gap-x-10" v-if="boolDetails.state == 0">
                                            <div class="flex flex-col ml-1">
                                                <label class="mt-2">Brand</label>
                                                <select
                                                    class="w-[8rem] h-[3rem] rounded-sm border-solid border border-black"
                                                    v-model="selectedBrand" @change="getSize(selectedBrand, -1)">
                                                    <option v-for="(tyre, index) in brand" :key="index">{{ tyre }}
                                                    </option>
                                                </select>
                                            </div>
                                            <div class="flex flex-col ml-1">
                                                <label class="mt-2">Variants</label>
                                                <select
                                                    class="w-[8rem] h-[3rem] rounded-sm border-solid border border-black"
                                                    v-model="selectedVariant"
                                                    @change="getPattern(selectedBrand, selectedVariant, index)">
                                                    <option v-for="(variant, index) in rs" :key="index">{{ variant.size
                                                        }}</option>
                                                </select>
                                            </div>
                                            <div class="flex flex-col ml-1">
                                                <label class="mt-2">Quantity</label>
                                                <input
                                                    class="w-[8rem] h-[3rem] rounded-sm border-solid border border-black"
                                                    type="number" v-model="quantity">
                                            </div>
                                            <div class="flex flex-col ml-1">
                                                <Button class="w-[4rem] mt-10" @click="addItem">Add</Button>
                                            </div>
                                            <div class="flex flex-col ml-1">
                                                <label class="mt-2">Pattern</label>
                                                <select
                                                    class="w-[8rem] h-[3rem] rounded-sm border-solid border border-black"
                                                    v-model="pattern"
                                                    @change="getType(selectedBrand, selectedVariant, pattern, index)">
                                                    <option v-for="(pattern, index) in patterns[index]" :key="index">{{
                                                        pattern
                                                        }}</option>
                                                </select>
                                            </div>
                                            <div class="flex flex-col ml-1">
                                                <label class="mt-2">Type</label>
                                                <select
                                                    class="w-[8rem] h-[3rem] rounded-sm border-solid border border-black"
                                                    v-model="type">
                                                    <option v-for="(type, index) in types[index]" :key="index">{{ type
                                                        }}</option>
                                                </select>
                                            </div>
                                        </div>
                                        <div v-if="tableDetails">
                                            <table class="table-auto">
                                                <thead>
                                                    <tr>
                                                        <th class="pr-12">Brand</th>
                                                        <th class="pr-12">Size</th>
                                                        <th class="pr-12">Quantity</th>
                                                        <th class="pr-12">Type</th>
                                                        <th>Pattern</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr v-for="(item, index) in items" :key="index">
                                                        <td>{{ item.brand }}</td>
                                                        <td>{{ item.variants }}</td>
                                                        <td>{{ item.quantity }}</td>
                                                        <td>{{ item.type }}</td>
                                                        <td>{{ item.pattern }}</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                        <div v-if="leadDetails && !tableDetails">
                                            <table class="table-auto">
                                                <thead>
                                                    <tr>
                                                        <th class="pr-12">Brand</th>
                                                        <th class="pr-12">Size</th>
                                                        <th class="pr-12">Quantity</th>
                                                        <th class="pr-12">Type</th>
                                                        <th>Pattern</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr v-for="(item, index) in leadDetails.custom_lead_items"
                                                        :key="index">
                                                        <td>{{ item?.brand }}</td>
                                                        <td>{{ item?.size }}</td>
                                                        <td v-if="item.brand && item.size">{{ item?.quantity }}</td>
                                                        <td>{{ item?.tyre_type }}</td>
                                                        <td>{{ item?.pattern }}</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                        <label class="font-semibold">Services</label>
                                        <hr class="dark-hr">
                                        <div class="grid grid-cols-3 mt-5">
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.alignment"
                                                    :checked="leadDetails.custom_alignment == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm"
                                                    id="alignment">
                                                <label class="p-2" for="alignment">Alignment</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.rotation"
                                                    :checked="leadDetails.custom_rotation == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm"
                                                    id="rotation">
                                                <label class="p-2" for="rotation">Rotation</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.oil_change"
                                                    :checked="leadDetails.custom_oil_change == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm"
                                                    id="oil_change">
                                                <label class="p-2" for="oil_change">Oil Change</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.balancing"
                                                    :checked="leadDetails.custom_balancing == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm"
                                                    id="balancing">
                                                <label class="p-2" for="balancing">Balancing</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.inflation"
                                                    :checked="leadDetails.custom_inflation == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm"
                                                    id="inflation">
                                                <label class="p-2" for="inflation">Inflation</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.puncture"
                                                    :checked="leadDetails.custom_puncture == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm"
                                                    id="puncture">
                                                <label class="p-2" for="puncture">Puncture</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.tyre_edge"
                                                    :checked="leadDetails.custom_tyre_edge == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm"
                                                    id="tyre_edge">
                                                <label class="p-2" for="tyre_edge">Tyre Edge</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.tyre_patch"
                                                    :checked="leadDetails.custom_tyre_patch == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm"
                                                    id="tyre_patch">
                                                <label class="p-2" for="tyre_patch">Tyre Patch</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.mushroom_patch"
                                                    :checked="leadDetails.custom_mushroom_patch == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm"
                                                    id="mushroom_patch">
                                                <label class="p-2" for="mushroom_patch">Mushroom Patch</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.ac_service"
                                                    :checked="leadDetails.custom_ac_service == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm"
                                                    id="ac_service">
                                                <label class="p-2" for="ac_service">AC Service</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.battery"
                                                    :checked="leadDetails.custom_battery == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm"
                                                    id="battery">
                                                <label class="p-2" for="battery">Battery</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.wiper"
                                                    :checked="leadDetails.custom_wiper == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm"
                                                    id="wiper">
                                                <label class="p-2" for="wiper">Wiper</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.car_wash"
                                                    :checked="leadDetails.custom_car_wash == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm"
                                                    id="car_wash">
                                                <label class="p-2" for="car_wash">Car Wash</label>
                                            </div>
                                        </div>
                                        <div>
                                            <button v-if="!mobileSearch"
                                                class="bg-green-500 w-[100%]  text-white font-bold 0 text-base p-4 rounded-lg m-3"
                                                @click="handleCustomer">Save</button>
                                            <button v-if="mobileSearch"
                                                class="bg-gray-500 w-[100%]  text-white font-bold 0 text-base p-4 rounded-lg m-3"
                                                @click="okCustomer">Ok</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div v-if="showModifyCustomer"
                            class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-end items-center pb-10">
                            <div class="fixed inset-0" @click="modifyCustomer"></div>
                            <div class="max-w-md w-full bg-white shadow-xl h-full overflow-y-auto relative">
                                <button class="absolute to text-black pt-5 font-bold right-2 px-2 py-1 rounded"
                                    @click="modifyCustomer">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M6 18L18 6M6 6l12 12" />
                                    </svg>
                                </button>
                                <div class="p-8 mt-[140px]">
                                    <h2 class="text-2xl font-semibold mb-4">Customer Details</h2>
                                    <hr class="dark-hr">
                                    <p class="m-2">Vehicle Number <br>
                                        <input type="text" v-if="check" v-model="responseData.message[1].name" disabled
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter Vehicle Number">
                                    </p>
                                    <p class="m-2">Owner Name <br>
                                        <input type="text" v-if="check" v-model="responseData.message[1].current_owner"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter Owner Name">
                                    </p>
                                    <p class="m-2">Owner Mobile No <br>
                                        <input type="tel" v-if="check" v-model="responseData.message[1].owner_mobile_no"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter Owner Mobile No.">
                                    </p>
                                    <input type="checkbox" v-if="check"
                                        :checked="responseData.message[1]?.whatsapp === 1"
                                        @change="responseData.message[1].whatsapp = $event.target.checked ? 1 : 0"
                                        class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>WhatsApp</label>
                                    <span class="ml-5">
                                        <input type="checkbox" v-if="check"
                                            :checked="responseData.message[1]?.call === 1"
                                            @change="responseData.message[1].call = $event.target.checked ? 1 : 0"
                                            class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>Call</label>
                                    </span>
                                    <span class="ml-5">
                                        <input type="checkbox" v-if="check"
                                            :checked="responseData.message[1]?.sms === 1"
                                            @change="responseData.message[1].sms = $event.target.checked ? 1 : 0"
                                            class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>SMS</label>
                                    </span>
                                    <div v-for="(employee, index) in responseData.message[1].current_driver"
                                        :key="index" class="mt-2">
                                        <hr class="dark-hr m-4">
                                        <p class="m-3">Employee Name
                                            <button
                                                class="bg-blue-500 w-[100px] text-white font-bold  text-base p-4 rounded-lg mb-1 float-right"
                                                @click="removeEmployee2(index)">Remove</button> <br>
                                            <input type="text" v-model="employee.current_driver"
                                                class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                                placeholder="Enter your Name">
                                        </p>
                                        <p class="m-2">Employee Type<br>
                                            <select v-model="employee.parentfield"
                                                @change="updateEmployeeType(employee)"
                                                class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black">
                                                <option :value="'current_driver'"
                                                    :selected="employee.parentfield === 'current_driver'">Driver
                                                </option>
                                                <option :value="'contact_person'"
                                                    :selected="employee.parentfield === 'contact_person'">Contact
                                                    Person
                                                </option>
                                            </select>
                                        </p>
                                        <p class="m-2">Phone <br>
                                            <input type="tel" v-model="employee.mobile_no"
                                                class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black">
                                        </p>
                                        <input type="checkbox" v-if="check" :checked="employee.whatsapp === 1"
                                            @change="employee.whatsapp = $event.target.checked ? 1 : 0"
                                            class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>WhatsApp</label>
                                        <span class="ml-5">
                                            <input type="checkbox" v-if="check" :checked="employee.call === 1"
                                                @change="employee.call = $event.target.checked ? 1 : 0"
                                                class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>Call</label>
                                        </span>
                                        <span class="ml-5">
                                            <input type="checkbox" v-if="check" :checked="employee.sms === 1"
                                                @change="employee.sms = $event.target.checked ? 1 : 0"
                                                class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>SMS</label>
                                        </span>
                                        <span class="ml-5">
                                            <input type="checkbox" v-if="check" :checked="employee.primary === 1"
                                                @change="employee.primary = $event.target.checked ? 1 : 0"
                                                @click="handlePrimaryCheckboxModify(employee)"
                                                class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>Primary</label>
                                        </span>
                                    </div>
                                    <div v-for="(contact, index) in responseData.message[1].contact_person" :key="index"
                                        class="mt-2">
                                        <hr class="dark-hr m-4">
                                        <p class="m-3">Employee Name
                                            <button
                                                class="bg-blue-500 w-[100px] text-white font-bold  text-base p-4 rounded-lg mb-1 float-right"
                                                @click="removeEmployee3(index)">Remove</button> <br>
                                            <input type="text" v-model="contact.contact_person_name"
                                                class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                                placeholder="Enter your Name">
                                        </p>
                                        <p class="m-2">Employee Type<br>
                                            <select v-model="contact.parentfield" @change="updateEmployeeType(contact)"
                                                class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black">
                                                <option :value="'current_driver'"
                                                    :selected="contact.parentfield === 'current_driver'">Driver
                                                </option>
                                                <option :value="'contact_person'"
                                                    :selected="contact.parentfield === 'contact_person'">Contact
                                                    Person
                                                </option>
                                            </select>
                                        </p>
                                        <p class="m-2">Phone <br>
                                            <input type="tel" v-model="contact.contact_person_mobile"
                                                class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black">
                                        </p>
                                        <input type="checkbox" v-if="check" :checked="contact.custom_whatsapp === 1"
                                            @change="contact.custom_whatsapp = $event.target.checked ? 1 : 0"
                                            class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>WhatsApp</label>
                                        <span class="ml-5">
                                            <input type="checkbox" v-if="check" :checked="contact.custom_call === 1"
                                                @change="contact.custom_call = $event.target.checked ? 1 : 0"
                                                class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>Call</label>
                                        </span>
                                        <span class="ml-5">
                                            <input type="checkbox" v-if="check" :checked="contact.custom_sms === 1"
                                                @change="contact.custom_sms = $event.target.checked ? 1 : 0"
                                                class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>SMS</label>
                                        </span>
                                        <span class="ml-5">
                                            <input type="checkbox" v-if="check" :checked="contact.custom_primary === 1"
                                                @change="contact.custom_primary = $event.target.checked ? 1 : 0"
                                                @click="handlePrimaryCheckboxModify(contact)"
                                                class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>Primary</label>
                                        </span>
                                    </div>
                                    <div class="mt-5">
                                        <button
                                            class="bg-blue-500 w-[40%] h-[3.2rem] text-white font-bold 0 text-base p-5 rounded-lg ml-3"
                                            @click="modifiedMoreEmployee('current_driver')">Add Driver</button>

                                        <button
                                            class="bg-blue-500 w-[50%] h-[3.2rem]  text-white font-bold 0 text-base p-5 rounded-lg ml-3"
                                            @click="modifiedMoreEmployee('contact_person')">Add Con.Person</button>
                                    </div>
                                    <div class="m-3 mt-[40px] flex flex-row space-x-[70px]">
                                        <button
                                            class="bg-green-500 w-[100px]  text-white font-bold 0 text-base p-4 rounded-lg ml-3"
                                            @click="addCustomerModifiedData">Save</button>
                                        <button
                                            class="bg-red-500 w-[100px]  text-white font-bold text-base p-4 rounded-lg ml-3"
                                            @click="removeModifiedCustomerData">Clear</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- 5 point checkup  -->
            <div v-if="currentstep == 1" class="mr-9">
                <div class="p-12 pt-24 w-screen ">
                    <div class="flex flex-row justify-between p-1">
                        <h1 class="text-[1.2rem] font-bold mt-5">5 Points Checkup</h1>
                    </div>
                    <hr class="mt-2 " :style="{ borderWidth: '2px', borderColor: 'gray' }">
                    <div class="grid grid-row space-y-5 mt-4  p-4 mr-[0.1rem] bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg"
                        v-for="(tyreData, index) in tyreDatas" :key="index">
                        <div class="flex">
                            <div class="grid grid-cols-4 w-[90%] gap-4">
                                <div class="flex flex-col space-y-1 ml-4">
                                    <label class="mt-2" :for="'tyre' + index">Tyre</label>
                                    <select class="w-[100%] h-[3.5rem] rounded-sm" v-model="tyreData.tyre"
                                        :id="'type' + index" style="border: 1px solid black;"
                                        @change="updateTyreData(index)">
                                        <option value="" selected disabled hidden>Please select...</option>
                                        <option value="Front Left">Front Left</option>
                                        <option value="Front Right">Front Right</option>
                                        <option value="Rear Left">Rear Left</option>
                                        <option value="Rear Right">Rear Right</option>
                                        <option value="Spare Tyre">Spare Tyre</option>
                                    </select>
                                </div>
                                <div class="flex flex-col space-y-1">
                                    <label class="mt-2" :for="'RTD' + index">Remaining Tread Depth
                                        <span v-if="tyreData.mandatory && !tyreData.depth.trim()"
                                            class="text-red-500 font-bold">*</span>
                                    </label>
                                    <input v-model="tyreData.depth"
                                        class="w-[100%] h-[3.5rem] rounded-sm border-solid border border-black"
                                        type="text" :id="'RTD' + index" @change="updateTyreData(index)">
                                </div>
                                <div class="flex flex-col space-y-1">
                                    <label class="mt-2" :for="'TP' + index">Tyre Pressure (psi)
                                        <span v-if="tyreData.mandatory && !tyreData.pressure.trim()"
                                            class="text-red-500 font-bold">*</span>
                                    </label>
                                    <input v-model="tyreData.pressure"
                                        class="w-[100%] h-[3.5rem] rounded-sm border-solid border border-black"
                                        type="text" :id="'TP' + index" @change="updateTyreData(index)">
                                </div>
                                <div class="flex flex-col space-y-1">
                                    <label class="mt-2" :for="'COM' + index">Comment
                                        <span v-if="tyreData.mandatory && !tyreData.comment.trim()"
                                            class="text-red-500 font-bold">*</span>
                                    </label>
                                    <input v-model="tyreData.comment"
                                        class="w-[100%] h-[3.5rem] rounded-sm border-solid border border-black"
                                        type="text" :id="'COM' + index" @change="updateTyreData(index)">
                                </div>
                            </div>
                            <div class="ml-9">
                                <FeatherIcon name="trash-2" class="mt-11 w-8 h-8 cursor-pointer text-red-500"
                                    @click="deleteTyre(index)" />
                            </div>
                        </div>
                        <div class="flex flex-row space-x-15">
                            <div class="flex flex-row items-center space-x-3 ml-4">
                                <input v-model="tyreData.wear" class="rounded-sm border border-black bg-gray-200"
                                    type="checkbox" id="IW">
                                <label for="IW">Irregular Wear</label>
                            </div>
                            <div class="flex flex-row items-center space-x-3">
                                <input v-model="tyreData.cut" class="rounded-sm border border-black bg-gray-200"
                                    type="checkbox" id="C/D">
                                <label for="C/D">Cut/Damage</label>
                            </div>
                            <div class="flex flex-row items-center space-x-3">
                                <input v-model="tyreData.mark" class="rounded-sm border border-black bg-gray-200"
                                    type="checkbox" id="RFM">
                                <label for="RFM">Run Flat MARK</label>
                            </div>
                            <div class="flex flex-row items-center space-x-3">
                                <input v-model="tyreData.damage" class="rounded-sm border border-black bg-gray-200"
                                    type="checkbox" id="DM">
                                <label for="DM">Damage</label>
                            </div>
                            <div class="flex flex-row items-center space-x-3">
                                <input v-model="tyreData.bulge" class="rounded-sm border border-black bg-gray-200"
                                    type="checkbox" id="BL">
                                <label for="BL">Bulge</label>
                            </div>
                            <div class="flex flex-row items-center space-x-3">
                                <input v-model="tyreData.puncture" class="rounded-sm border border-black bg-gray-200"
                                    type="checkbox" id="PUN">
                                <label for="PUN">Puncture</label>
                            </div>
                            <div class="flex flex-row items-center space-x-3">
                                <button class="bg-gray-600 text-white rounded-lg p-1 font-bold"
                                    @click="clearData(index)">Clear</button>
                            </div>
                        </div>
                    </div>
                    <div class="mt-5">
                        <button class="text-[1.2rem]  text-white w-[12rem] h-[3rem] bg-blue-500 rounded-lg"
                            @click="addTyre">Add</button>
                    </div>
                </div>
            </div>
            <!-- Required Services -->
            <div v-if="currentstep == 2">
                <div class="pt-24">
                    <div class=" p-12">
                        <h1 class="text-[20px] font-bold mb-1">Required Services</h1>
                        <hr class="mt-2" :style="{ borderWidth: '2px', borderColor: 'gray' }">
                        <div
                            class="mt-6 flex flex-row space-x-[12rem] p-7 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg">
                            <!-- col-1 -->
                            <div class="flex flex-col space-y-4 mt-4">
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.alignment_service_checkbox" id="alignment"
                                        @change="handleShow('alignment')">
                                    <label class="text-[18px]" for="alignment">Alignment</label>
                                </div>
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.rotation_service_checkbox" id="rotation"
                                        @change="handleShow('rotation')">
                                    <label class="text-[18px]" for="rotation">Rotation</label>
                                </div>
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.oil_change_service_checkbox" id="oil_change"
                                        @change="handleShow('oil_change')">
                                    <label class="text-[18px]" for="oil_change">Oil Change</label>
                                </div>
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.balancing_service_checkbox" id="balancing"
                                        @change="handleShow('balancing')">
                                    <label class="text-[18px]" for="balancing">Balancing</label>
                                </div>
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.inflation_service_checkbox" id="inflation"
                                        @change="handleShow('inflation')">
                                    <label class="text-[18px]" for="inflation">Inflation</label>
                                </div>
                            </div>
                            <!-- col-2 -->
                            <div class="flex flex-col space-y-4 mt-4">
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.puncture_checkbox" id="puncture"
                                        @change="handelCheck('puncture')">
                                    <label class="text-[18px]" for="puncture">Puncture</label>
                                </div>
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.tyre_edge_checkbox" id="tyre_edge"
                                        @change="handelCheck('tyre_edge')">
                                    <label class="text-[18px]" for="tyre_edge">Tyre Edge</label>
                                </div>
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.tyre_path_checkbox" id="tyre_batch"
                                        @change="handelCheck('tyre_patch')">
                                    <label class="text-[18px]" for="tyre_batch">Tyre Patch</label>
                                </div>
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.mushroom_path_checkbox" id="mushroom_patch"
                                        @change="handelCheck('mushroom_patch')">
                                    <label class="text-[18px]" for="mushroom_patch">Mushroom Patch</label>
                                </div>
                            </div>
                            <!-- col-3 -->
                            <div class="flex flex-col space-y-4 mt-4">
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.ac_service_checkbox" id="ac_service"
                                        @change="handleShow('ac_service')">
                                    <label class="text-[18px] pr-[7px]" for="ac_service">AC Service</label>&emsp;
                                    <!-- <select v-if="show.Ac" class="w-[16rem] h-[3rem] rounded-sm"
                                        style="border: 1px solid black;" v-model="requireService.ac" @change="shooo">
                                        <option value="" selected disabled hidden>Please select...</option>
                                        <option value="good">Good</option>
                                        <option value="better">Better</option>
                                        <option value="not_good">Not Good</option>
                                    </select> -->
                                </div>
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.battery_service_checkbox" id="battery"
                                        @change="handleShow('battery')">
                                    <label class="text-[18px] pr-1" for="battery">Battery</label>&emsp;&emsp;&emsp;
                                    <!-- <select v-if="show.battery" class="w-[16rem] h-[3rem] rounded-sm"
                                        style="border: 1px solid black;" v-model="requireService.battery"
                                        @change="shooo">
                                        <option value="" selected disabled hidden>Please select...</option>
                                        <option value="good">Good</option>
                                        <option value="better">Better</option>
                                        <option value="not_good">Not Good</option>
                                    </select> -->
                                </div>
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.wiper_service_checkbox" id="wiper" @change="handleShow('wiper')">
                                    <label class="text-[18px] pr-[1px]"
                                        for="wiper">Wiper</label>&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;
                                    <!-- <select v-if="show.wiper" class="w-[16rem] h-[3rem] rounded-sm"
                                        style="border: 1px solid black;" v-model="requireService.wiper" @change="shooo">
                                        <option value="" selected disabled hidden>Please select...</option>
                                        <option value="good">Good</option>
                                        <option value="better">Better</option>
                                        <option value="not_good">Not Good</option>
                                    </select> -->
                                </div>
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.car_wash_service_checkbox" id="car_wash"
                                        @change="handleShow('car_wash')">
                                    <label class="text-[18px] pr-[2px]" for="car_wash">Car Wash</label>&emsp;&emsp;
                                    <!-- <select v-if="show.car_wash" class="w-[16rem] h-[3rem] rounded-sm"
                                        style="border: 1px solid black;" v-model="requireService.car_wash"
                                        @change="shooo">
                                        <option value="" selected disabled hidden>Please select...</option>
                                        <option value="good">Good</option>
                                        <option value="better">Better</option>
                                        <option value="not_good">Not Good</option>
                                    </select> -->
                                </div>
                            </div>
                        </div>
                        <!-- hiden fields -->
                        <div class="flex flex-col space-y-6 mt-6 ">
                            <div v-if="show.alignment"
                                class="p-6 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg">
                                <h1 class="text-[20px] font-bold ml-1 mb-6">Alignment Details</h1>
                                <div class="flex flex-row space-x-[12rem] ml-[55px]">
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[16px]" for="LA">Last Alignment (kms)<span
                                                v-if="requireService.mandatory && !requireService.alignments.lastAlignment.trim()"
                                                class="text-red-500 font-bold">*</span></label>
                                        <input class="w-[16rem]] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="LA" v-model="requireService.alignments.lastAlignment">
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[16px]" for="NA">Next Alignment (kms)<span
                                                v-if="requireService.mandatory && !requireService.alignments.nextAlignment.trim()"
                                                class="text-red-500 font-bold">*</span></label>
                                        <input class="w-[16rem]] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="NA" v-model="requireService.alignments.nextAlignment"
                                            @change="shooo">
                                    </div>
                                </div>
                            </div>
                            <div v-if="show.rotation"
                                class="p-6 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg">
                                <h1 class="text-[20px] font-bold ml-1 mb-6">Tyre Rotation Details</h1>
                                <div class="flex flex-row space-x-[12rem] ml-[55px]">
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[16px]" for="inche">Inche
                                            <span
                                                v-if="requireService.mandatory && !requireService.rotations.inche.trim()"
                                                class="text-red-500 font-bold">*</span>
                                        </label>
                                        <!-- <input class="w-[16rem]] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="inche" v-model="requireService.rotations.inche"> -->
                                        <select class="w-[16rem] h-[3rem] rounded-sm border-solid border border-black"
                                            id="inche" v-model="requireService.rotations.inche">
                                            <option value="" disabled selected>Select an Inche</option>
                                            <option v-for="inch in R_inch" :key="inch" :value="inch">{{ inch }}</option>
                                        </select>
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[16px]" for="wheel">Wheel Count
                                            <span
                                                v-if="requireService.mandatory && !requireService.rotations.wheel_count"
                                                class="text-red-500 font-bold">*</span>
                                        </label>
                                        <input class="w-[16rem]] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="wheel" v-model='requireService.rotations.wheel_count'
                                            @change="shooo">
                                    </div>
                                </div>
                            </div>
                            <div v-if="show.oil_change"
                                class="p-6 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg">
                                <h1 class="text-[20px] font-bold ml-1 mb-6">Oil Service</h1>
                                <div class="flex flex-row space-x-[12rem] ml-[55px]">
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[16px]" for="oil_quality">Oil Quality
                                            <span
                                                v-if="requireService.mandatory && !requireService.oil_changes.oil_quality.trim()"
                                                class="text-red-500 font-bold">*</span>
                                        </label>
                                        <div>
                                            <select class="w-[15rem] h-[3rem] rounded-sm"
                                                style="border: 1px solid black;" id="oil_quality"
                                                v-model="requireService.oil_changes.oil_quality">
                                                <option value="" selected disabled hidden>Please select...</option>
                                                <option value="Good">Good</option>
                                                <option value="Ok">Ok</option>
                                                <option value="Change">Change</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[16px]" for="oil_quantity">Oil Quantity
                                            <span
                                                v-if="requireService.mandatory && !requireService.oil_changes.oil_quantity.trim()"
                                                class="text-red-500 font-bold">*</span>
                                        </label>
                                        <div>
                                            <select class="w-[15rem] h-[3rem] rounded-sm"
                                                style="border: 1px solid black;" id="oil_quantity"
                                                v-model="requireService.oil_changes.oil_quantity" @change="shooo">
                                                <option value="" selected disabled hidden>Please select...</option>
                                                <option value="Max">Max</option>
                                                <option value="Normal">Normal</option>
                                                <option value="Min">Min</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div v-if="show.balancing"
                                class="p-6 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg">
                                <h1 class="text-[20px] font-bold ml-1 mb-6">Balancing Details
                                </h1>

                                <div class="flex flex-row justify-around">
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[1rem]" for="FL">Inches
                                            <span v-if="requireService.mandatory && !requireService.balancings.inches"
                                                class="text-red-500 font-bold">*</span>
                                        </label>
                                        <!-- <input class="w-[12rem] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="FL" v-model="requireService.balancings.inches"> -->
                                        <select class="w-[16rem] h-[3rem] rounded-sm border-solid border border-black"
                                            id="inche" v-model="requireService.balancings.inches">
                                            <option value="" disabled selected>Select an Inche</option>
                                            <option v-for="inch in B_inch" :key="inch" :value="inch">{{ inch }}</option>
                                        </select>
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[1rem]" for="FL">Type
                                            <span
                                                v-if="requireService.mandatory && !requireService.balancings.type.trim()"
                                                class="text-red-500 font-bold">*</span>
                                        </label>
                                        <div>
                                            <select class="w-[15rem] h-[3rem] rounded-sm"
                                                style="border: 1px solid black;" id="type"
                                                v-model="requireService.balancings.type">
                                                <option value="" selected disabled hidden>Please select...</option>
                                                <option value="Ordinary">Ordinary</option>
                                                <option value="Alloy">Alloy</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                                <input type="checkbox" class="w-5 h-5 rounded-sm border border-black bg-gray-200"
                                    @change="handleGrams()" v-model="requireService.balancings.gramsCheck"
                                    id="Grams"><label for="Grams" class="text-[18px] pl-[12px]">Grams</label>
                                <div class="flex flex-row justify-around mt-5" v-if="showGrams">
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[1rem]" for="FL">Front-Left (gm)
                                        </label>
                                        <input class="w-[12rem] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="FL" v-model="requireService.balancings.fl">
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[1rem]" for="FR">Front-Right (gm)
                                        </label>
                                        <input class="w-[12rem] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="FR" v-model="requireService.balancings.fr">
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[1rem]" for="BL">Back-Left (gm)
                                        </label>
                                        <input class="w-[12rem] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="BL" v-model="requireService.balancings.bl">
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[1rem]" for="BR">Back-Right (gm)
                                        </label>
                                        <input class="w-[12rem] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="BR" v-model="requireService.balancings.br">
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[1rem]" for="ST">Spare Tyre (gm)
                                        </label>
                                        <input class="w-[12rem] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="ST" v-model='requireService.balancings.st' @change="shooo">
                                    </div>
                                </div>
                            </div>
                            <div v-if="show.inflation"
                                class="p-6 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg">
                                <h1 class="text-[20px] font-bold ml-1 mb-6">Inflation Details</h1>
                                <div class="flex flex-row space-x-[100px] ml-[55px]">
                                    <div class="flex flex-col space-y-5">
                                        <div class="flex flex-row space-x-3 mt-3">
                                            <input class="w-5 h-5 rounded-sm border border-black bg-gray-200"
                                                type="checkbox" id="air" :checked="selectedCheckbox === 'air'"
                                                @change="handleCheckboxChange('air')" v-model="show.inflation_air">
                                            <label class="text-[18px]" for="air">Air</label>
                                        </div>
                                        <div class="flex flex-row space-x-3">
                                            <input class="w-5 h-5 rounded-sm border border-black bg-gray-200"
                                                type="checkbox" id="nitrogen" :checked="selectedCheckbox === 'nitrogen'"
                                                @change="handleCheckboxChange('nitrogen')"
                                                v-model="show.inflation_nitrogen">
                                            <label class="text-[18px]" for="nitrogen">Nitrogen</label>
                                        </div>
                                    </div>
                                    <div class="flex flex-row space-x-[100px]">
                                        <div class="flex flex-col space-y-1">
                                            <label class="text-[16px]" for="FTS">Front Tyres (psi)
                                                <span
                                                    v-if="requireService.mandatory && !requireService.inflations.ft.trim()"
                                                    class="text-red-500 font-bold">*</span>
                                            </label>
                                            <input
                                                class="w-[12rem]] h-[3rem] rounded-sm border-solid border border-black"
                                                type="text" id="FTS" v-model="requireService.inflations.ft">
                                        </div>
                                        <div class="flex flex-col space-y-1">
                                            <label class="text-[16px]" for="RTS">Rear Tyres (psi)
                                                <span
                                                    v-if="requireService.mandatory && !requireService.inflations.rt.trim()"
                                                    class="text-red-500 font-bold">*</span>
                                            </label>
                                            <input
                                                class="w-[12rem]] h-[3rem] rounded-sm border-solid border border-black"
                                                type="text" id="RTS" v-model="requireService.inflations.rt"
                                                @change="shooo">
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Replacement Tyre Details -->
            <div v-if="currentstep == 3">
                <div class="pt-24 p-12">
                    <div class="flex flex-row justify-between">
                        <h1 class="text-[20px] font-bold mb-1">Tyre Replacement Details</h1>
                    </div>
                    <hr class="mt-2 " :style="{ borderWidth: '2px', borderColor: 'gray' }">
                    <div class="pb-5 ">
                        <div v-for="(tyre, index) in tyres" :key="index"
                            class="grid grid-cols-10 gap-[11rem] mt-7 pb-5 ml-2 border-b border-gray-900 p-2 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg">
                            <div class="ml-5 w-[16rem]">
                                <label class="pt-2" :for="'type' + index">Tyre Position</label><br>
                                <select class="w-[15rem] h-[52px] rounded-sm border-solid border border-black"
                                    v-model="tyre.type" :id="'type' + index">
                                    <option value="" selected disabled hidden>Please select...</option>
                                    <option value="Front Left">Front Left</option>
                                    <option value="Front Right">Front Right</option>
                                    <option value="Rear Left">Rear Left</option>
                                    <option value="Rear Right">Rear Right</option>
                                    <option value="Spare Tyre">Spare Tyre</option>
                                </select>
                                <div class="mt-[20px]">
                                    <label :for="'loadIndex' + index">Load Index<span
                                            v-if="tyre.mandatory && !tyre.loadIndex.trim()"
                                            class="text-red-500 font-bold">*</span></label><br>
                                    <input class="w-[15rem] h-[52px] rounded-sm border-solid border border-black"
                                        :id="'loadIndex' + index" type="text" v-model="tyre.loadIndex"
                                        @change="saveData(index)">
                                </div>
                            </div>
                            <div class="ml-[100px]">
                                <div>
                                    <label :for="'brand' + index">Brand<span v-if="tyre.mandatory && !tyre.brand.trim()"
                                            class="text-red-500 font-bold">*</span></label>
                                    <select class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                        v-model="tyre.brand" @change="getSize(tyre.brand, index)">
                                        <option v-for="(tyre, index) in brand" :key="index">{{ tyre }}</option>
                                    </select>
                                </div>
                                <div class="mt-[20px] w-[16rem]">
                                    <label :for="'speedRating' + index">Speed Rating<span
                                            v-if="tyre.mandatory && !tyre.speedRating.trim()"
                                            class="text-red-500 font-bold">*</span></label>
                                    <input class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                        :id="'speedRating' + index" type="text" v-model="tyre.speedRating"
                                        @change="saveData(index)">
                                </div>
                            </div>
                            <div class="ml-[200px]">
                                <div>
                                    <label :for="'size' + index">Size<span v-if="tyre.mandatory && !tyre.size.trim()"
                                            class="text-red-500 font-bold">*</span></label>
                                    <select class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                        v-model="tyre.size" @change="getOther(tyre.brand, tyre.size, index)">
                                        <option v-for="(size, index) in sizes[index]" :key="index">{{ size.size }}
                                        </option>
                                    </select>
                                </div>
                                <div class="mt-[20px]">
                                    <div>
                                        <label :for="'ttTl' + index">TT/TL<span
                                                v-if="tyre.mandatory && !tyre.ttTl.trim()"
                                                class="text-red-500 font-bold">*</span></label>
                                        <select class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                            v-model="tyre.ttTl"
                                            @change="getItemCode(tyre.brand, tyre.size, tyre.ttTl, tyre.pattern, index)">
                                            <option v-for="(type, index) in types[index]" :key="index">{{ type }}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                            <div class="ml-[300px]">
                                <label :for="'pattern' + index">Pattern<span
                                        v-if="tyre.mandatory && !tyre.pattern.trim()"
                                        class="text-red-500 font-bold">*</span></label>
                                <select class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                    v-model="tyre.pattern"
                                    @change="getType(tyre.brand, tyre.size, tyre.pattern, index)">
                                    <option v-for="(pattern, index) in patterns[index]" :key="index">{{ pattern }}
                                    </option>
                                </select>
                                <div class="mt-[20px]">
                                    <label :for="'pattern' + index">Warranty(in_Years)<span
                                            v-if="tyre.mandatory && !tyre.warranty.trim()"
                                            class="text-red-500 font-bold">*</span></label>
                                    <!-- <span>(upto_{{maxYears}})</span> -->
                                    <input type="text"
                                        class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                        v-model="tyre.warranty" @keyup="warrantyYears(tyre.warranty)">
                                </div>
                            </div>
                            <div class="ml-[400px] mt-5">
                                <FeatherIcon name="trash-2" class="mt-0 ml-2 w-6 h-6 cursor-pointer text-red-500"
                                    @click="deleteTyreReplacement(index)" />
                                <div class="mt-[80px]">
                                    <button class="bg-gray-600 text-white rounded-lg p-1 font-bold"
                                        @click="clearTyreData(index)">Clear</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <button class=" text-[1.2rem]  text-white w-[12rem] h-[3rem] bg-blue-500 rounded-lg"
                            @click="addTyreReplacement">Add</button>
                    </div>
                </div>
            </div>
            <!-- Billing Details -->
            <div v-if="currentstep == 4" @click="dataLoaded = false; billCustomer = ''">
                <div v-if="showConfirm"
                    class="fixed inset-1 overflow-hidden bg-black bg-opacity-50 flex justify-center items-center">
                    <div class="bg-white rounded-lg p-8 shadow-xl">
                        <h2 class="text-xl font-semibold mb-4">Confirm Save</h2>
                        <p class="mb-4">Are you sure want to save the details?</p>
                        <div class="flex justify-center">
                            <button @click="confirmDataSave"
                                class="bg-green-500 text-white font-semibold px-4 py-2 rounded mr-2">Save</button>
                            <button @click="cancelSaved"
                                class="bg-red-500 text-white font-semibold px-4 py-2 rounded">Cancel</button>
                        </div>
                    </div>
                </div>
                <div v-if="showpop"
                    class="fixed inset-1 overflow-hidden bg-black bg-opacity-50 flex justify-center items-center">
                    <div class="bg-white rounded-lg p-8 shadow-xl">
                        <h2 class="text-xl font-semibold mb-4">Confirm Save</h2>
                        <p class="mb-4">Are you sure want to save the details?</p>
                        <div class="flex justify-center">
                            <button @click="confirmBill(), respop = ''"
                                class="bg-green-500 text-white font-semibold px-4 py-2 rounded mr-2">Save</button>
                            <button @click="showpop = false"
                                class="bg-red-500 text-white font-semibold px-4 py-2 rounded">Cancel</button>
                        </div>
                    </div>
                </div>
                <div v-if="cancelpop"
                    class="fixed inset-1 overflow-hidden bg-black bg-opacity-50 flex justify-center items-center">
                    <div class="bg-white rounded-lg p-8 shadow-xl">
                        <h2 class="text-xl font-semibold mb-4">Confirm Cancel</h2>
                        <p class="mb-4">Are you sure want to cancel the details?</p>
                        <div class="flex justify-center">
                            <button
                                @click="currentstep = 0; cancelpop = false; tableData = []; selectedname = ''; selectednumber = ''; totalRate = 0, totalQuantity = 0, totalCost = 0, finalAmount = 0, respop = '', directCancel()"
                                class="bg-green-500 text-white font-semibold px-4 py-2 rounded mr-2">Yes</button>
                            <button @click="cancelpop = false"
                                class="bg-red-500 text-white font-semibold px-4 py-2 rounded">No</button>
                        </div>
                    </div>
                </div>
                <div v-if="finalSuccess"
                    class="fixed inset-1 overflow-hidden bg-black bg-opacity-50 flex justify-center items-center">
                    <div class="bg-white rounded-lg p-8 shadow-xl">
                        <h2 class="text-xl font-semibold mb-4 text-green-600">Data added Successfully!</h2>
                    </div>
                </div>
                <div class="pt-24 p-12">
                    <div v-if="newpop"
                        class="fixed inset-1 overflow-hidden bg-black bg-opacity-50 flex justify-center items-center">
                        <div class="bg-white rounded-lg p-12 shadow-x">
                            <div class="text-red-500 mb-4">
                                <h6 class="flex justify-center">{{ customerResponse }}</h6>
                            </div>
                            <h2 class="text-3xl font-semibold mb-3 mr-4">New Customer</h2>
                            <div class="mb-2 ml-20rem">
                                <p>Customer Name <span v-if="mentatory && !newName" class="text-red-500">*</span></p>
                                <input type="text" class="w-[100%] h-[3rem] rounded-sm border-solid border border-black"
                                    v-model="newName" />
                            </div>
                            <div class="mb-3">
                                <p>Customer Mobile No <span v-if="mentatory && !newNumber" class="text-red-500">*</span>
                                </p>
                                <input type="tel" class="w-[100%] h-[3rem] rounded-sm border-solid border border-black"
                                    v-model="newNumber" @input="customerResponse = ''" />
                            </div>
                            <div class="flex justify-center">
                                <button @click="newCustomer"
                                    class="bg-green-500 w-[9rem] text-white font-semibold px-4 py-2 rounded mr-2">Save</button>
                                <button @click="newpop = false; mentatory = false"
                                    class="bg-red-500 w-[9rem] text-white font-semibold px-4 py-2 rounded">Cancel</button>
                            </div>
                        </div>
                    </div>
                    <div v-if="billing === true">
                        <h1 class="text-[20px] font-bold mb-1">Customer Deatils</h1>
                        <hr class="mt-2" :style="{ borderWidth: '2px', borderColor: 'gray' }">
                        <div class="custom-dropdown">
                            <input type="text" placeholder="Search..." v-model="billCustomer" @input="checkcustomer"
                                class="custom-input w-[100%] h-[2.5rem] rounded-sm border-solid border border-black">
                            <ul v-show="dataLoaded" class="custom-dropdown-list">
                                <li v-for="option in customers" :key="option.value" @click="selectOption(option)"
                                    class="custom-dropdown-item">
                                    <div v-if="option.customer_name">
                                        <label>{{ option.customer_name }}</label><br>
                                        <label>{{ option.mobile_no }}</label>
                                    </div>
                                    <div v-if="!option.customer_name">
                                        <label>No data found</label>
                                    </div>
                                </li>
                            </ul>
                            <button class="bg-blue-500 text-white font-bold text-base p-3 rounded-sm mt-3"
                                @click="addNew()">Create
                                Customer</button>
                        </div>
                        <label><span v-if="respop && !selectedname" class="text-red-500">{{ respop }}</span></label>
                        <div class="mt-3" v-if="selectedname && selectednumber">
                            <div>
                                <label>Name :</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                <label>{{ selectedname }}</label>
                            </div>
                            <div class="mt-1">
                                <label>Phone No :</label>&nbsp;&nbsp;
                                <label>{{ selectednumber }}</label>
                            </div>
                        </div>
                    </div>
                    <h1 class="text-[20px] font-bold mb-1">Items</h1>
                    <hr class="mt-2" :style="{ borderWidth: '2px', borderColor: 'gray' }">
                    <div class="pt-5">
                        <table
                            class="table-auto border border-collapse border-gray-800 w-auto shadow-md transition-shadow">
                            <thead>
                                <tr>
                                    <th class="border border-gray-800 px-4 py-4 w-[10rem]">SI.No</th>
                                    <th class="border border-gray-800 px-4 py-4 w-[10rem]">Item<span v-if="itempop"
                                            class="text-red-500">*</span></th>
                                    <th class="border border-gray-800 px-4 py-4 w-[16rem]">Warehouse<span v-if="warepop"
                                            class="text-red-500">*</span></th>
                                    <th class="border border-gray-800 px-4 py-4 w-[10rem]">Warranty(in_years)</th>
                                    <th class="border border-gray-800 px-4 py-4 w-[16rem]">Quantity<span v-if="qutpop"
                                            class="text-red-500">*</span></th>
                                    <th class="border border-gray-800 px-4 py-4 w-[10rem]">Rate</th>
                                    <th class="border border-gray-800 px-4 py-4 w-[10rem]">Amount</th>
                                </tr>
                            </thead>
                            <pre>{{ tableData.value }}</pre>
                            <tbody class="border border-gray-800 text-center">
                                <tr v-for="(data, index) in tableData" :key="index">
                                    <td class="border border-gray-800 px-4 py-2 w-[10rem]">{{ index + 1 }}</td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <!-- <input type="text" v-model="data[0].itemCode"
                                            class="w-[10rem] rounded-sm border-solid border border-black"> -->
                                        <select v-model="data[0].itemCode"
                                            @change="get_itemrate($event.target.value, index); itempop = ''; billpop = '';"
                                            class="w-[10rem] rounded-sm border-solid border border-black">
                                            <option value="">Select Item</option>
                                            <!-- Loop through billitems and create an option for each item -->
                                            <option v-for="(item) in billitems" :key="item.id" :value="item.name">
                                                {{ item.name }}
                                            </option>
                                        </select>


                                    </td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <div style="max-height: 200px; overflow-y: auto;">
                                            <select v-model="data[0].sourceWarehouse"
                                                class="w-[10rem] rounded-sm border-solid border border-black"
                                                @change="warepop = ''; bilpop = ''">
                                                <option value="">Select Warehouse</option>
                                                <!-- Loop through warehouseList and create an option for each warehouse -->
                                                <option v-for="warehouse in Warehouse" :key="warehouse"
                                                    :value="warehouse">
                                                    {{ warehouse }}
                                                </option>
                                            </select>
                                        </div>
                                    </td>

                                    <td class="border border-gray-800 px-4 py-2">
                                        <input type="number" v-model="data[0].warranty"
                                            @input="calculateTotals(); qutpop = ''; billpop = ''"
                                            class="w-[10rem] rounded-sm border-solid border border-black">
                                    </td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <input type="number" v-model="data[0].requiredQuantity"
                                            @input="calculateTotals(); qutpop = ''; billpop = ''"
                                            class="w-[10rem] rounded-sm border-solid border border-black">
                                    </td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <input type="float" v-model="data[0].rate" @input="calculateTotals" readonly
                                            class="w-[10rem] h-[2.6rem] pl-[0.7rem] rounded-sm border-solid border border-black text-justify">
                                    </td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <input type="text" v-model="data[0].cost" readonly
                                            class=" w-[10rem] rounded-sm border-solid border border-black cursor-not-allowed">
                                    </td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <button
                                            class="w-[5rem] bg-red-500 text-white font-bold text-base p-3 rounded-lg mt-3"
                                            @click="removeRow(index)">Delete</button>
                                    </td>
                                </tr>
                            </tbody>
                            <tfoot>
                                <tr>
                                    <td colspan="3" class="border border-gray-800 px-4 py-2 text-center">
                                        Total
                                    </td>
                                    <td class="border border-gray-800 px-4 py-2 text-center cursor-not-allowed">
                                        {{ warranty }}
                                    </td>
                                    <td class="border border-gray-800 px-4 py-2 text-center cursor-not-allowed">
                                        {{ totalQuantity }}
                                    </td>
                                    <td colspan=""
                                        class="border border-gray-800 px-4 py-2 text-center cursor-not-allowed">
                                        {{ totalRate.toFixed(2) }}
                                    </td>
                                    <td colspan="2"
                                        class="border border-gray-800 px-4 py-2 text-center cursor-not-allowed">
                                        {{ totalCost.toFixed(2) }}
                                    </td>
                                </tr>
                            </tfoot>
                        </table>
                        <label><span v-if="billpop" class="text-red-500">{{ billpop }}</span></label>
                        <div class="mb-9">
                            <button class="bg-blue-500 text-white font-bold text-base p-3 rounded-lg mt-3"
                                @click="addNewRow(billIndex); billpop = ''">Add row</button>
                        </div>
                        <div class="flex">
                            <label>Discount Rate: <input type="text" v-model="discountRate"
                                    @input="calculateDiscountRate"
                                    class="w-[338px] h-[52px] rounded-sm border-solid border border-black"></label>
                            <label class="ml-auto pr-5">Total Amount:
                                <input type="text" :value="finalAmount" readonly
                                    class="w-[338px] h-[52px] rounded-sm border-solid border border-black cursor-not-allowed">
                            </label>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="Auth">
                <div class="flex justify-center space-x-5 p-5 mt-5 ml-3">
                    <button v-if="currentstep != 0 && billing !== true"
                        class="bg-blue-500 w-[45%] text-white font-bold  text-base p-4 rounded-lg"
                        @click="previousPage">Previous
                    </button>
                    <button v-if="currentstep != 4 && initialNext && nextButtonEnable"
                        class="bg-blue-500 w-[45%] text-white font-bold  text-base p-4 rounded-lg"
                        @click="nextPageAndHighlight">Next
                    </button>
                    <button v-if="currentstep == 4 && billing !== true" @click="dataFinalSubmission"
                        class="bg-green-700 w-[45%] text-white font-bold  text-base p-4 rounded-lg">
                        Submit
                    </button>
                    <button v-if="currentstep != 0 && billing === true"
                        class="bg-red-500 w-[45%] text-white font-bold  text-base p-4 rounded-lg"
                        @click="cancelpop = true">Cancel
                    </button>
                    <button v-if="currentstep == 4 && billing === true" @click="finalSubmit"
                        class="bg-green-700 w-[45%] text-white font-bold  text-base p-4 rounded-lg">
                        Submit
                    </button>
                </div>
                <div class="bottom-div">
                    <div class="bottom-div">
                        <div class="m-0 p-4">
                            <ul class="ml-[100px] flex space-x-[120px] text-center">
                                <li type="disc" :class="{ 'active': currentPage === 'details' }"
                                    @click="setCurrentPage('details', 0)">Details</li>
                                <li type="disc" :class="{ 'active': currentPage === '5 Points Checkup' }"
                                    @click="setCurrentPage('5 Points Checkup', 1)" :disabled="initialNext">5 Points
                                    Checkup</li>
                                <li type="disc" :class="{ 'active': currentPage === 'Required Services' }"
                                    @click="setCurrentPage('Required Services', 2)" :disabled="initialNext">Required
                                    Services</li>
                                <li type="disc" :class="{ 'active': currentPage === 'Tyre Replacement Details' }"
                                    @click="setCurrentPage('Tyre Replacement Details', 3)" :disabled="initialNext">Tyre
                                    Replacement Details</li>
                                <li type="disc" :class="{ 'active': currentPage === 'Billing Details' }"
                                    @click="setCurrentPage('Billing Details', 4)" :disabled="initialNext">Billing
                                    Details</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive, watch, computed, onMounted, watchEffect } from 'vue';
import { FeatherIcon } from 'frappe-ui'
import axios from 'axios';

const selectImg = ref(true);
const Auth = ref(true)
const incorrect = ref(false);
const currentstep = ref(0);

const data = reactive({
    selectedImgSrc: '',
    selectedAlt: ''
});

const billing = ref(false)
const billCustomer = ref('');

const headers = {
    'Content-Type': 'application/json',

    'Authorization': 'token b89ae1f0409875e :af8a0b78d948ebf'

}

const pin1 = ref('');
const pin2 = ref('');
const pin3 = ref('');
const pin4 = ref('');
const items = ref([])
const tableDetails = ref(false);
const addItem = () => {
    tableDetails.value = true;
    if (selectedBrand.value && selectedVariant.value && quantity.value && type.value && pattern.value) {
        items.value.push({
            brand: selectedBrand.value,
            variants: selectedVariant.value,
            quantity: quantity.value,
            type: type.value,
            pattern: pattern.value
        });
    }
};

function handleImgSelection(event) {
    selectImg.value = true;
    data.selectedImgSrc = event.target.src;
    data.selectedAlt = event.target.alt;
}

const customers = ref([])
const dataLoaded = ref(false)
const selectedname = ref('')
const selectednumber = ref('')
const selecteddoc = ref('')

function selectOption(data) {
    selecteddoc.value = data.name;
    selectedname.value = data.customer_name;
    selectednumber.value = data.mobile_no;
    console.log(data, "data")
    dataLoaded.value = false;
    billCustomer.value = '';
}

//==========menu  icon=========//
const item = ref([
    { title: 'Billing' },
    { title: 'Sales Invoices' },
    { title: 'Paid Invoices' },
    { title: 'Enquiry List' },
    { title: 'Job Card List' },
])

const showMenu = ref(false)

const toggleMenu = () => {
    showMenu.value = !showMenu.value
}




function checkcustomer() {
    console.log(billCustomer)
    axios.post(`${BaseURL}/api/method/tyre.api.get_customer`, { data: billCustomer.value }, { headers: headers })
        .then(response => {
            console.log(response.data.message)
            customers.value = response.data.message
            console.log("Customer", customers.value)
            dataLoaded.value = true
        })
}
const billitems = ref([]);

onMounted(() => {
    axios.get(`${BaseURL}/api/method/tyre.api.get_items`, { headers: headers })
        .then(response => {
            console.log(response.data.message);
            // brand.value = response.data.message;
            billitems.value = response.data.message;
            console.log(billitems.value)
        })
});
const B_inch = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22];
const R_inch = ref([])
onMounted(() => {
    axios.get(`${BaseURL}/api/method/tyre.api.get_inch_list`, { headers: headers })
        .then(response => {
            R_inch.value = response.data.message;
        })
});

const newpop = ref(false)
const newName = ref('')
const newNumber = ref('')

function addNew() {
    console.log("create new")
    newpop.value = true
    newName.value = ''
    newNumber.value = ''
}

const mentatory = ref(false)
const customerResponse = ref('')

function newCustomer() {
    if (newName.value && newNumber.value) {
        console.log("created")
        axios.post(`${BaseURL}/api/method/tyre.api.create_customer`, { name: newName.value, no: newNumber.value }, { headers: headers })
            .then(response => {
                if (response.data.message === "Customer created successfully") {
                    newpop.value = false
                    selectedname.value = newName.value
                    selectednumber.value = newNumber.value
                } else {
                    customerResponse.value = response.data.message;
                }
            })
    } else {
        mentatory.value = true
    }
}

const showpop = ref(false)
const cancelpop = ref(false)
const respop = ref('')
const billpop = ref('')
const itempop = ref(false)
const warepop = ref(false)
const qutpop = ref(false)

function finalSubmit() {
    if (selectedname.value && selectednumber.value) {
        if (tableData.value.length !== 0) {
            console.log(tableData.value)
            for (let i = 0; i < tableData.value.length; i++) {
                if (!tableData.value[i][0].itemCode && !tableData.value[i][0].sourceWarehouse && !tableData.value[i][0].requiredQuantity) {
                    console.log("no data")
                    billpop.value = "Fill the require fields...!"
                    itempop.value = true;
                    warepop.value = true
                    qutpop.value = true
                    break;
                } else if (!tableData.value[i][0].itemCode && !tableData.value[i][0].sourceWarehouse) {
                    billpop.value = "Fill the require fields...!"
                    itempop.value = true;
                    warepop.value = true
                    break;
                } else if (!tableData.value[i][0].sourceWarehouse && !tableData.value[i][0].requiredQuantity) {
                    billpop.value = "Fill the require fields...!"
                    warepop.value = true
                    qutpop.value = true
                    break;
                } else if (!tableData.value[i][0].itemCode && !tableData.value[i][0].requiredQuantity) {
                    billpop.value = "Fill the require fields...!"
                    itempop.value = true;
                    qutpop.value = true
                    break;
                }

            }
            console.log(billpop.value)
            if (!billpop.value) {
                showpop.value = true;
            }
        } else {
            billpop.value = "Add billing data...!";
        }
    } else {
        respop.value = "Select a customer...!"
    }
}

function confirmBill() {
    console.log(tableData.value)
    console.log(selectedname.value)
    console.log(selectednumber.value)
    console.log(selecteddoc.value)
    axios.post(`${BaseURL}/api/method/tyre.api.sales_order`, { data: tableData.value, name: selecteddoc.value }, { headers: headers })
        .then(response => {
            if (response.data.message === "done") {
                showpop.value = false
                finalSuccess.value = true
                console.log(tableData.value)
                setTimeout(() => {
                    finalSuccess.value = false;
                    currentstep.value = 0
                    selectedname.value = ''
                    selectednumber.value = ''
                    tableData.value = []
                    totalQuantity.value = '';
                    totalRate.value = 0.00;
                    totalCost.value = 0.00;
                    finalAmount.value = 0.00;
                    step = 0;
                    window.location.reload()
                }, 2000);
            }
        })
}
const directCancel = () => {
    window.location.reload();
}

function focusNext(event, nextInput) {
    const target = event.target;
    if (target.value.length === 1) {
        const inputs = target.parentNode.querySelectorAll('input');
        if (nextInput < inputs.length) {
            inputs[nextInput].focus();
        } else {
            submitPin();
        }
    }
}

function submitPin() {
    if (pin1 && pin2 && pin3 && pin4) {
        const pin = pin1.value + pin2.value + pin3.value + pin4.value;
        if (pin === "1234") {
            Auth.value = true;
        }
        else {
            incorrect.value = true;
            pin1.value = pin2.value = pin3.value = pin4.value = '';
            setTimeout(() => {
                incorrect.value = false;
            }, 3000);
        }
    }
}

const jobCard = {}
const brand = ref([])
const rs = ref([])
const sizes = ref([])
const patterns = ref([])
const types = ref([])
const Warehouse = ref([])
const vBrand = ref([])
const vModel = ref([])
const BaseURL = window.location.origin

onMounted(() => {
    axios.get(`${BaseURL}/api/method/tyre.api.get_brand`, { headers: headers })
        .then(response => {
            brand.value = response.data.message;
        })
});

onMounted(() => {
    axios.get(`${BaseURL}/api/method/tyre.api.get_warehouse`, { headers: headers })
        .then(response => {
            Warehouse.value = response.data.message
        })
})

onMounted(() => {
    axios.get(`${BaseURL}/api/method/tyre.api.get_vehicleBrand`, { headers: headers })
        .then(response => {
            vBrand.value = response.data.message
        })
})


const get_Vmodel = (data) => {
    axios.post(`${BaseURL}/api/method/tyre.api.get_vehicleModel`, { model: data }, { headers: headers })
        .then(response => {
            vModel.value = response.data.message
        })
}

const getSize = (data, index) => {
    axios.post(`${BaseURL}/api/method/tyre.api.get_size`, { brand: data }, { headers: headers })
        .then(response => {
            if (index != -1) {
                sizes.value[index] = response.data.message;
            } else {
                rs.value = response.data.message;
            }
        })
}

const getOther = (brand, data, index) => {
    let i = 0;
    for (const co in sizes.value[index]) {
        const sizeData = sizes.value[index][i]
        if (sizeData.size == data) {
            tyres.value[index].loadIndex = sizeData.load_index;
            tyres.value[index].speedRating = sizeData.speed_rating;
            // getType(brand, data, index)
            getPattern(brand, data, index)
        }
        i++;
    }
}
const getType = (brand, data, pattern, index) => {
    axios.post(`${BaseURL}/api/method/tyre.api.get_type`, { brand: brand, size: data, pattern: pattern }, { headers: headers })
        .then(response => {
            types.value[index] = response.data.message;
        });
}
const getPattern = (brand, size, index) => {
    axios.post(`${BaseURL}/api/method/tyre.api.get_pattern`, { brand: brand, size: size }, { headers: headers })
        .then(response => {
            patterns.value[index] = response.data.message;
        });
}
const getItemCode = (brand, size, type, pattern, index) => {
    axios.post(`${BaseURL}/api/method/tyre.api.get_ItemCode`, { brand: brand, size: size, tyer_type: type, pattern: pattern }, { headers: headers })
        .then(response => {
            tyres.value[index].item = response.data.message[0]
            tyres.value[index].rate = response.data.message[1]
        });

}
//==========================================================>>> Main Page <<<================================================================================//
const initial = ref(true);
const initialNext = ref(false);
const hasResponse = ref(true);
const noData = ref(false);
const successData = ref(false);
const searchValue = ref(false);
const noMessage = ref(false);
const showMessage = () => {
    noMessage.value = true;
    setTimeout(() => {
        noMessage.value = false;
    }, 1000);
};

const isEditMode = ref(false)
const searchQuery = ref('');
const responseData = ref({});


const spacing = (plate) => {
    const spaced_plate = plate.match(/[a-zA-Z]{1,2}|\d+/g).join(" ");
    return spaced_plate;
};

const dataAssignment = (response) => {
    responseData.value = {
        message: [
            response.data.message[0],
            response.data.message[1] ? response.data.message[1] : {
                current_owner: '',
                owner_mobile_no: '',
                call: '',
                whatsapp: '',
                sms: '',
                current_driver: [{
                    current_driver: '',
                    name: '',
                    mobile_no: '',
                    call: '',
                    whatsapp: '',
                    sms: ''

                }],
                contact_person: [{
                    contact_person_name: '',
                    contact_person_mobile: '',
                    custom_call: '',
                    custom_whatsapp: '',
                    custom_sms: ''
                }]
            },
            response.data.message[2] ? response.data.message[2] : {
                current_driver: [{
                    current_driver: '',
                    name: '',
                    mobile_no: '',
                    call: '',
                    whatsapp: '',
                    sms: ''

                }],
                contact_person: [{
                    contact_person_name: '',
                    contact_person_mobile: '',
                    custom_call: '',
                    custom_whatsapp: '',
                    custom_sms: ''
                }]
            }
        ]
    };
    console.log('customer_mobile_no', responseData.value.message[1]?.owner_mobile_no)
    return responseData.value;
}
const check = ref(false)
const checked = ref(false)
const wrongSearchValue = ref(false);
const enable = ref(false)
const nextButtonEnable = ref(false)

const search = async () => {
    const data = {
        "license_plate": searchQuery.value
    };
    try {
        if (data.license_plate.trim() !== "") {
            const response = await axios.post(`${BaseURL}/api/method/tyre.api.get_details`, { license_plate: data.license_plate }, { headers: headers });
            if (response.data.message === "Enter a Valid vehicle number") {

                check.value = false;
                showAlerts.value = true;
                wrongSearchValue.value = true;
                setTimeout(() => {
                    showAlerts.value = false;
                    wrongSearchValue.value = false;
                }, 1000);
                hasResponse.value = true;
                initial.value = true;
                initialNext.value = false
                searchQuery.value = ''
                setTimeout(() => {
                    noData.value = false;
                }, 2000);
                // The entire UI will show no data if searchdata has no value.
                return dataAssignment(response)
            }

            else if (response.data.message == '') {
                check.value = false;
                enable.value = false;
                noData.value = true;
                initialNext.value = false
                setTimeout(() => {
                    noData.value = false;
                }, 2000);
                hasResponse.value = true;
                initial.value = true;
            }

            else {
                check.value = true;
                checked.value = true;
                enable.value = true;
                hasResponse.value = false;
                initial.value = false;
                afterResponse.value = true;
                initialNext.value = true
                searchQuery.value = ''
                nextButtonEnable.value = true;
                enquiryPage.value = false;
                searchMobileAfterResponse.value = false;
                console.log("response", response.data.message)
                return dataAssignment(response)
            }
        } else {
            showAlerts.value = true;
            searchValue.value = true;
            setTimeout(() => {
                showAlerts.value = false;
                searchValue.value = false;
            }, 1000);
        }
    } catch (error) {
        console.error("Error:", error);
    }
};

const searchJobCard = ref('')
const hide = ref('false');
const jobCardDetails = reactive(ref([]));
const searchShow = ref(true);
const getJobCard = async () => {
    hide.value = true;
    check.value = false;
    initialNext.value = false;
    searchShow.value = false;
    try {
        const response = await axios.post(`${BaseURL}/api/method/tyre.api.get_jobcard_details`, { searchJobCard: searchJobCard.value }, { headers: headers });
        jobCardDetails.value = response.data.message;
        console.log("jobcard details", jobCardDetails.value);
        if (responseData && responseData.value && responseData.value.message && responseData.value.message[0]?.name) {
            nextButtonEnable.value = true;
        } else {
            nextButtonEnable.value = false;
        }
    }
    catch (error) {
        console.error("Error:", error);
    }
}

const searchEnquiry = ref('');
const hideEnq = ref('false');
const enquiryDetails = reactive(ref([]));
const getEnquiry = async () => {
    hideEnq.value = true;
    check.value = false;
    initialNext.value = false;
    searchShow.value = false;
    try {
        const response = await axios.get(`${BaseURL}/api/method/tyre.api.get_enquiry_details`, {
            params: {
                data: searchEnquiry.value
            },
            headers: headers
        });
        enquiryDetails.value = response.data.message;
        if (responseData && responseData.value && responseData.value.message && responseData.value.message[0]?.name) {
            nextButtonEnable.value = true;
        } else {
            nextButtonEnable.value = false;
        }
    } catch (e) {
        console.error("Error:", e);
    }
}

const jobCardPopup = ref('false');
const jobCardData = ref([]);
const fetchJobCard = async (id) => {
    try {
        const response = await axios.get(`${BaseURL}/api/method/tyre.api.get_billing_details`, {
            params: {
                name: id
            },
            headers: headers
        });
        jobCardPopup.value = 'true'
        jobCardData.value = response.data.message;
        console.log("job card data", jobCardData.value);
    }
    catch (error) {
        console.error("Error:", error);
    }
}
const enquiryPopup = ref('false');
const enquiryData = ref([]);
const fetchEnquiry = async (id) => {
    try {
        const response = await axios.get(`${BaseURL}/api/method/tyre.api.get_enquiry`, {
            params: {
                name: id
            },
            headers: headers
        });
        enquiryPopup.value = 'true'
        enquiryData.value = response.data.message;
        console.log("enquirydata", enquiryData.value)
    }
    catch (error) {
        console.error("Error:", error);
    }
}

watch(searchJobCard, () => {
    getJobCard();
});

watch(searchEnquiry, () => {
    getEnquiry();
});

const currentPage = ref('details');
const maxStep = 4;

function previousPage() {
    if (currentstep.value > 0) {
        currentstep.value--;
        currentPage.value = getPageName(currentstep.value);
    }
}

const showWarning = ref(false)
function nextPageAndHighlight() {
    console.log(billIndex, "billIndex-kp")
    if (currentstep.value < maxStep) {
        currentstep.value++;
        currentPage.value = getPageName(currentstep.value);
        switch (currentstep.value) {
            case 1:
                jobCard["user"] = responseData.value.message[0].name;
                break;
            case 2:
                jobCard["checkup"] = tyreDatas.value;
                for (let i = 0; i < tyreDatas.value.length; i++) {
                    const tyre = tyreDatas.value[i];
                    if (tyre.tyre) {
                        if (tyre.comment == '' || tyre.depth == '' || tyre.pressure == '') {
                            tyre.mandatory = true;
                            currentstep.value = 1;
                            return;
                        }
                    }
                    else {
                        tyre.mandatory = false
                    }
                }
                break;
            case 3:
                jobCard["service"] = requireService.value
                requireService.value.mandatory = false;

                if (requireService.value.Alignment &&
                    (!requireService.value.alignments.lastAlignment || !requireService.value.alignments.nextAlignment)) {
                    requireService.value.mandatory = true;
                    currentstep.value = 2;
                    return;
                }
                else {
                    requireService.value.mandatory = false;
                }

                if (requireService.value.Rotation &&
                    (!requireService.value.rotations.inche || !requireService.value.rotations.wheel_count)) {
                    requireService.value.mandatory = true;
                    currentstep.value = 2;
                    return;
                }

                if (requireService.value.Oil_change &&
                    (!requireService.value.oil_changes.oil_quality || !requireService.value.oil_changes.oil_quantity)) {
                    requireService.value.mandatory = true;
                    currentstep.value = 2;
                    return;
                }

                if (requireService.value.Balancing &&
                    (!requireService.value.balancings.inches || !requireService.value.balancings.type)) {
                    requireService.value.mandatory = true;
                    currentstep.value = 2;
                    return;
                }


                if (requireService.value.Inflation &&
                    (!requireService.value.inflations.type || !requireService.value.inflations.ft || !requireService.value.inflations.rt)) {
                    requireService.value.mandatory = true;
                    currentstep.value = 2;
                    return;
                }
                addValue(requireService.value, replace)
                console.log("checking requireservice data for inches and type in balancing", requireService.value)
                break;
            case 4:
                jobCard["replace"] = tyres.value
                for (let i = 0; i < tyres.value.length; i++) {
                    const tyre = tyres.value[i];
                    if (tyre.type) {
                        if (tyre.loadIndex == '' || tyre.brand == '' || tyre.speedRating == '' || tyre.size == '' || tyre.pattern == '' || tyre.ttTl == '' || tyre.warranty == '') {
                            tyre.mandatory = true;
                            currentstep.value = 3;
                            return;
                        }
                    }
                    else {
                        tyre.mandatory = false
                    }
                }
                addValue(tyres.value, replace)
                console.log(jobCard)
                break;
            case 5:
                checkup(jobCard);
                console.log("final jobcard data", jobCard);
                break;
        }
    }
}

function getPageName(step) {
    switch (step) {
        case 0:
            return 'details';
        case 1:
            return '5 Points Checkup';
        case 2:
            return 'Required Services';
        case 3:
            return 'Tyre Replacement Details';
        case 4:
            return 'Billing Details';
        default:
            return 'details';
    }
}

const setCurrentPage = (page, step) => {
    if (initialNext.value && nextButtonEnable.value) {
        currentPage.value = page;
        currentstep.value = step;
    }
};
const vehicleDetails = ref({
    name: '',
    vehicle_brand: '',
    vehicle_model: '',
    fuel_type: '',
    last_odometer_reading: '',
    tyre_change: '',
    alignment: ''
})


const showNewVehicle = ref(false);
const showNewCustomer = ref(false)
const showModifyVehicle = ref(false);
const showModifyCustomer = ref(false);

const addVehicle = () => {
    showNewVehicle.value = !showNewVehicle.value;
};
const addCustomer = () => {
    showNewCustomer.value = !showNewCustomer.value;
}
const modifyVehicle = () => {
    showModifyVehicle.value = !showModifyVehicle.value;
}
const modifyCustomer = () => {
    showModifyCustomer.value = !showModifyCustomer.value;
}

const vehicleData = ref({
    name: responseData?.message?.[0]?.name ?? '',
    vehicle_brand: '',
    vehicle_model: '',
    fuel_type: '',
    last_odometer_reading: '',
    tyre_change: '',
    alignment: ''
});

const showConfirmation = ref(false);
const newVehicleSave = ref(false);
const showAlerts = ref(false)
const vehicleNumber = ref(false)
const vehicleExist = ref(false)
const modifyAlert = ref(false);
const notVehicleAlert = ref(false);
const notCustomerAlert = ref(false)
const notEmployeeAlert = ref(false)
const notEmpDetailAlert = ref(false)
const noVehicleNumber = ref(false)
const noValidVehicleNumber = ref(false)
const noCustomerValidVehicleNumber = ref(false)
const cannotSave = ref(false)
const customerExist = ref(false)
const showDeleteConfirmation = ref(false)


const addVehicleData = async () => {
    const fieldNames = Object.keys(vehicleData.value);
    const data = {};
    let allRequiredFileds = true;

    fieldNames.forEach(fieldName => {
        const value = vehicleData.value[fieldName];
        if (value == '') {
            allRequiredFileds = false;
            return;
        }
        data[fieldName] = value;
    });

    const searchData = data.name;
    if (!searchData) {
        showNewVehicle.value = false
        showAlerts.value = true
        vehicleNumber.value = true
        return;
    }

    const isVehicleExist = await returnSearch(searchData);
    const checkingVehicleExist = isVehicleExist && isVehicleExist.message && isVehicleExist.message.length > 0 ? isVehicleExist.message == "Enter a Valid vehicle number" ? 'no data' : isVehicleExist.message[0].name : 'empty'
    if (checkingVehicleExist && checkingVehicleExist !== 'empty') {
        showNewVehicle.value = false
        showAlerts.value = true
        vehicleExist.value = true
        setTimeout(() => {
            showAlerts.value = false
            vehicleExist.value = false
            showNewVehicle.value = true
        }, 1000);
        return;
    }
    else if (isVehicleExist && isVehicleExist == 'Enter a Valid vehicle number') {
        showAlerts.value = true;
        noValidVehicleNumber.value = true;
    }
    else if (!allRequiredFileds) {
        showNewVehicle.value = false;
        showAlerts.value = true;
        vehicleNumber.value = true;
        setTimeout(() => {
            showAlerts.value = false;
            vehicleNumber.value = false;
            showNewVehicle.value = true;
        }, 1000);
    }
    else {
        showConfirmation.value = true;
        newVehicleSave.value = true;
        showNewVehicle.value = false;
    }
};

const confirmSave = async () => {
    showConfirmation.value = false;
    newVehicleSave.value = false;
    const fieldNames = Object.keys(vehicleData.value);
    const data = {};

    fieldNames.forEach(fieldName => {
        const value = vehicleData.value[fieldName];
        if (value == '') {
            return;
        }
        data[fieldName] = value;
    });
    const searchData = data.name;
    try {
        const response = await axios.post(`${BaseURL}/api/method/tyre.api.store_vehicle_details`, { data: JSON.stringify(data) }, { headers: headers });
        if (response) {
            enable.value = true;
            check.value = true;
            hasResponse.value = false;
            showAlerts.value = true
            successData.value = true;
            enquiryPage.value = false;
            afterResponse.value = true;
            checked.value = true;
            setTimeout(() => {
                showAlerts.value = false;
                successData.value = false;
            }, 1000);
            nextButtonEnable.value = true;
            dataAssignment(response);
            clearVehicleData();
            returnSearch(searchData);
        } else {
            check.value = false;
            console.error("responseData.value or responseData.value.message is undefined");
        }
    } catch (error) {
        console.error(error);
    }
};

const cancelSave = () => {
    showConfirmation.value = false;
    enable.value = false;
    clearVehicleData();
};

const addModifiedData = async () => {
    const name = responseData.value.message[1].name
    const modifiedData = {
        name: responseData.value.message[0].name,
        vehicle_brand: responseData.value.message[0].vehicle_brand,
        vehicle_model: responseData.value.message[0].vehicle_model,
        fuel_type: responseData.value.message[0].fuel_type,
        last_odometer_reading: responseData.value.message[0].last_odometer_reading,
        tyre_change: responseData.value.message[0].tyre_change,
        alignment: responseData.value.message[0].alignment
    };
    try {
        const response = await axios.post(`${BaseURL}/api/method/tyre.api.store_vehicle_details`, { data: JSON.stringify(modifiedData) }, { headers: headers });
        returnSearch(name)
        showModifyVehicle.value = false;
        showAlerts.value = true;
        modifyAlert.value = true;
        setTimeout(() => {
            showAlerts.value = false;
            modifyAlert.value = false;
        }, 1000);
    } catch (error) {
        console.error(error);
    }
};

const updateEmployeeType = (employee) => {
    return employee.parentfield
}

let primaryValue = reactive(ref(false))
const sample22 = reactive(ref(0))
const employees = ref([{
    driver_name: '',
    type: '',
    mobile_no: '',
    whatsappChecked1: 0,
    callChecked1: 0,
    smsChecked1: 0,
    primary: ref(primaryValue),
}]);
const customerData = ref({
    name: '',
    current_owner: '',
    owner_mobile_no: '',
    employees: employees.value,
    whatsappChecked: 0,
    callChecked: 0,
    smsChecked: 0,
});

const setPrimary = (index) => {
    let firstDriverIndex = -1;
    let firstContactPersonIndex = -1;

    customerData.value.employees.forEach((employee, i) => {
        if (employee.type === 'current_driver' && firstDriverIndex === -1) {
            firstDriverIndex = i;
        } else if (employee.type === 'contact_person' && firstContactPersonIndex === -1) {
            firstContactPersonIndex = i;
        }
    });

    if (index === firstDriverIndex || index === firstContactPersonIndex) {
        customerData.value.employees[index].primary = true;
    } else {
        console.log(`No primary found for index ${index}.`);
    }
};


function moreEmployee() {
    employees.value.push({
        driver_name: '',
        type: '',
        mobile_no: '',
        whatsappChecked1: 0,
        callChecked1: 0,
        smsChecked1: 0,
        primary: 0
    });
}

const modifiedMoreEmployee = async (type) => {
    try {
        const newEmployee = {
            mobile_no: '',
            current_driver: '',
            name: '',
            type: type,
        };

        if (type === 'current_driver') {
            const lastDriverIndex = responseData.value.message[1].current_driver.length - 1;
            newEmployee.whatsapp = responseData.value.message[1].current_driver[lastDriverIndex]?.whatsapp;
            newEmployee.call = responseData.value.message[1].current_driver[lastDriverIndex]?.call;
            newEmployee.sms = responseData.value.message[1].current_driver[lastDriverIndex]?.sms;
            if (newEmployee.whatsapp || newEmployee.call || newEmployee.sms) {
                newEmployee.whatsapp = 0;
                newEmployee.call = 0;
                newEmployee.sms = 0;
                responseData.value.message[1].current_driver.push(newEmployee);
            } else {
                responseData.value.message[1].current_driver.push(newEmployee);
            }
        } else if (type === 'contact_person') {
            const lastContactIndex = responseData.value.message[1].contact_person.length - 1;
            newEmployee.custom_whatsapp = responseData.value.message[1].contact_person[lastContactIndex]?.custom_whatsapp;
            newEmployee.custom_call = responseData.value.message[1].contact_person[lastContactIndex]?.custom_call;
            newEmployee.custom_sms = responseData.value.message[1].contact_person[lastContactIndex]?.custom_sms;
            if (newEmployee.custom_whatsapp || newEmployee.custom_call || newEmployee.custom_sms) {
                newEmployee.custom_whatsapp = 0;
                newEmployee.custom_call = 0;
                newEmployee.custom_sms = 0;
                responseData.value.message[1].contact_person.push(newEmployee);
            } else {
                responseData.value.message[1].contact_person.push(newEmployee);
            }
        } else {
            console.error('Invalid employee type:', type);
            return;
        }
    } catch (error) {
        console.error('Error adding more employees:', error);
    }
};

const leadDetails = ref([])
const handlePrimaryCheckbox = (clickedEmployee) => {
    if (clickedEmployee.type === 'contact_person') {
        employees.value.forEach(employee => {
            if (employee.type === 'contact_person' && employee !== clickedEmployee) {
                employee.primary = false;
            }
        });
    } else if (clickedEmployee.type === 'current_driver') {
        employees.value.forEach(employee => {
            if (employee.type === 'current_driver' && employee !== clickedEmployee) {
                employee.primary = false;
            }
        });
    }
};
const handlePrimaryCheckboxModify = (clickedEmployee) => {
    if (clickedEmployee.parentfield === 'contact_person') {
        responseData.value.message[1]?.contact_person.forEach(employee => {
            if (employee !== clickedEmployee) {
                employee.custom_primary = false;
            }
        });
    } else if (clickedEmployee.parentfield === 'current_driver') {
        responseData.value.message[1]?.current_driver.forEach(employee => {
            if (employee !== clickedEmployee) {
                employee.primary = false;
            }
        });
    }
};
const mobileNumber = ref(false)
const existMobileNumber = async (mobile) => {
    const data = {
        mobile: mobile,
    }
    const response = await axios.post(`${BaseURL}/api/method/tyre.api.exist_mobile_number`, { data: JSON.stringify(data) }, { headers: headers })
    if (response.data.message == "mobileExist") {
        showNewCustomer.value = false;
        showAlerts.value = true;
        mobileNumber.value = true;
        setTimeout(() => {
            showAlerts.value = false;
            mobileNumber.value = false;
            showNewCustomer.value = true;
        }, 1000);
        return true;
    }
    return false;
}

const addCustomerData = async () => {
    const name = responseData.value.message[0].name.trim();
    const existingData = await returnSearch(name);
    const mobileNumberExist = await existMobileNumber(customerData.value.owner_mobile_no)
    if (mobileNumberExist) {
        return
    }
    console.log("existing vehicle check", existingData)
    if (existingData.message[0].name && !existingData.message[1].current_owner) {
        const ownerName = customerData.value.current_owner.trim();
        const ownerMobile = customerData.value.owner_mobile_no.trim();

        if (!ownerName && !ownerMobile) {
            showAlerts.value = true;
            notCustomerAlert.value = true
            showNewCustomer.value = false
            setTimeout(() => {
                showAlerts.value = false;
                notCustomerAlert.value = false;
                showNewCustomer.value = true;
            }, 1000);
            return;
        }
        // if (employees.value.length === 0) {
        //     showNewCustomer.value = false
        //     showAlerts.value = true
        //     notEmployeeAlert.value = true
        //     setTimeout(() => {
        //         showAlerts.value = false;
        //         notEmployeeAlert.value = false;
        //         showNewCustomer.value = true;
        //     }, 1000);
        //     return;
        // }
        const isAnyEmployeeDataMissing = employees.value.some(employee => {
            return !employee.driver_name.trim() || !employee.mobile_no.trim();
        });
        if (isAnyEmployeeDataMissing) {
            showAlerts.value = true;
            notEmpDetailAlert.value = true;
            showNewCustomer.value = false
            setTimeout(() => {
                showAlerts.value = false;
                notEmpDetailAlert.value = false;
                showNewCustomer.value = true;
            }, 1000);
            return;
        }
        const data = {
            current_owner: customerData.value.current_owner,
            owner_mobile_no: customerData.value.owner_mobile_no,
            name: name,
            whatsappChecked: customerData.value.whatsappChecked,
            callChecked: customerData.value.callChecked,
            smsChecked: customerData.value.smsChecked,
            employees: []
        };

        employees.value.forEach(employee => {
            data.employees.push({
                driver_name: employee.driver_name,
                mobile_no: employee.mobile_no,
                type: employee.type,
                whatsappChecked1: employee.whatsappChecked1,
                callChecked1: employee.callChecked1,
                smsChecked1: employee.smsChecked1,
                primary: employee.primary
            });
        });
        try {
            const response = await axios.post(`${BaseURL}/api/method/tyre.api.store_customer_details`, { data: JSON.stringify(data) }, { headers: headers })
            check.value = true;
            console.log("customer details", response);
            if (response.data.message == "driver already exist") {
                alert("driver already exist")
            }
            else if (response.data.message == "contact person already exist") {
                alert("contact person already exist")
            }
            else if (response) {
                showNewCustomer.value = false;
                dataAssignment(response)
                showAlerts.value = true;
                successData.value = true;
                setTimeout(() => {
                    showAlerts.value = false;
                    successData.value = false;
                }, 1000);
                removeCustomerData()
                if (name) {
                    returnSearch(name)
                }
            } else {
                console.log("responseData.value or responseData.value.message is undefined");
            }

        } catch (error) {
            console.log('add customer error:', error);
        }
    }
    else {
        showNewCustomer.value = false;
        showAlerts.value = true
        customerExist.value = true
        setTimeout(() => {
            showAlerts.value = false
            customerExist.value = false
            showNewCustomer.value = true;

        }, 1000);
    }
};

const addCustomerModifiedData = async () => {
    const name = responseData.value.message[1].name
    const modifiedData = {
        name: responseData.value.message[1].name,
        current_owner: responseData.value.message[1].current_owner,
        owner_data: responseData.value.message[1].owner_data,
        owner_mobile_no: responseData.value.message[1].owner_mobile_no,
        whatsapp: responseData.value.message[1].whatsapp,
        call: responseData.value.message[1].call,
        sms: responseData.value.message[1].sms,
        employees: []
    };

    const driver = responseData.value.message[1].current_driver;
    const contactPerson = responseData.value.message[1].contact_person;


    driver.forEach((employee, index) => {
        let i = index
        const name = employee?.current_driver?.trim();
        if (name !== '') {
            modifiedData.employees.push({
                current_driver: name || '',
                name: responseData.value.message[1].current_driver[0].name ? responseData.value.message[1].current_driver[i].name : '',
                type: updateEmployeeType(employee) || '',
                mobile_no: employee.mobile_no || '',
                whatsapp: employee.whatsapp,
                call: employee.call,
                sms: employee.sms,
                primary: employee.primary,
                key: i
            });
        }
        else {
            return
        }
        i += 1;
    });
    contactPerson.forEach((employee, index) => {
        let i = index
        const name = employee?.contact_person_name?.trim();
        if (name !== '') {
            modifiedData.employees.push({
                contact_person_name: name || '',
                name: responseData.value.message[1].contact_person[0].name ? responseData.value.message[1].contact_person[i].name : '',
                type: updateEmployeeType(employee) || '',
                contact_person_mobile: employee.contact_person_mobile || '',
                custom_whatsapp: employee.custom_whatsapp,
                custom_call: employee.custom_call,
                custom_sms: employee.custom_sms,
                custom_primary: employee.custom_primary,
                key: i
            });
        }
        else {
            return
        }
        i += 1;
    });

    try {
        console.log("customer modified data before sending", modifiedData);
        const response = await axios.post(`${BaseURL}/api/method/tyre.api.store_customer_details`, { data: JSON.stringify(modifiedData) }, { headers: headers });
        console.log("customer details", response);
        if (response.data.message == "driver already exist") {
            alert("driver already exist")
        }
        else if (response.data.message == "contact person already exist") {
            alert("contact person already exist")
        }
        else if (response) {
            check.value = true;
            returnSearch(name)
            showModifyCustomer.value = false;
            showAlerts.value = true;
            modifyAlert.value = true;
            setTimeout(() => {
                showAlerts.value = false;
                modifyAlert.value = false;
            }, 1000);
        }
    } catch (error) {
        console.error("Error while processing request:", error.message);
    }
};

const removeModifiedCustomerData = () => {
    responseData.value.message[1].current_owner = '';
    responseData.value.message[1].owner_mobile_no = '';
    responseData.value.message[1].employees = [];
}

const clearModifiedVehicleData = () => {
    Object.keys(vehicleDetails.value).forEach(key => {
        vehicleDetails.value[key] = '';
    });
}
const responseTyreData = ref({})
const handle = ref(false);
const selectedVariant = ref(null);
const selectedBrand = ref(null);
const quantity = ref('');
const type = ref('');
const pattern = ref('');
const serviceDetails = ref({
    alignment: false,
    oil_change: false,
    inflation: false,
    tyre_edge: false,
    mushroom_patch: false,
    battery: false,
    car_wash: false,
    rotation: false,
    balancing: false,
    puncture: false,
    tyre_patch: false,
    ac_service: false,
    wiper: false
})
const leadCustomer = ref(false);
const handleCustomer = async () => {
    showNewCustomer.value = false;
    if (customerData.value.current_owner && customerData.value.owner_mobile_no) {
        const customerDetails = {
            current_owner: customerData.value.current_owner,
            owner_mobile_no: customerData.value.owner_mobile_no,
            whatsapp: customerData.value.whatsappChecked,
            call: customerData.value.callChecked,
            sms: customerData.value.smsChecked,
            items: items.value,
            services: {}
        }
        for (const key in serviceDetails.value) {
            if (Object.hasOwnProperty.call(serviceDetails.value, key)) {
                customerDetails.services[key] = serviceDetails.value[key];
            }
        }

        console.log('servicedetails', serviceDetails.value);
        console.log('customerDetails', customerDetails);
        console.log('customerDetails.services', customerDetails.services);
        try {
            const response = await axios.post(`${BaseURL}/api/method/tyre.api.lead`, customerDetails, { headers: headers })
            console.log("lead response", response.data);
            console.log("lead response item", response.data.message.lead_item);
            if (response.data.message.message == "Lead Created Successfully") {
                popItems.value = response.data.message;
                console.log("popitems", popItems.value)
                billPopup.value = 'true';
            } else if (response.data.message.message == "Lead Already Exists") {
                showNewCustomer.value = false;
                showAlerts.value = true;
                leadCustomer.value = true;
                setTimeout(() => {
                    showNewCustomer.value = true;
                    showAlerts.value = false;
                    leadCustomer.value = false;
                }, 1000);
                return
            }
            // if (responseData && responseData.messsage) {
            //    console.log('........');
            //    enquiryPage.value = false
            // }
        } catch (error) {
            console.log("Temporary customer details page:", error)
        }
    }
    else {
        showWarning.value = true;
        setTimeout(() => {
            showWarning.value = false;
            showNewCustomer.value = true;
        }, 1000);
    }
    return
}
const popItems = ref([]);
const billPopup = ref('false');

const deleteEnquiry = async () => {
    await axios.post(`${BaseURL}/api/method/tyre.api.delete_lead`, { data: popItems.value.name }, { headers: headers })
    billPopup.value = 'false';
    showNewCustomer.value = true;
    // hasResponse.value = true;
}

const enquiryClear = async () => {
    const data = {
        mobile_no: customerData.value.owner_mobile_no,
    };
    console.log("before whatsapp integration enquiry", data.mobile_no)
    try {
        const response = await axios.post(`${BaseURL}/api/method/tyre.api.send_quotation`, { data: JSON.stringify(data) }, { headers: headers })
        console.log("enquiry whatsapp integration success:", response);
    } catch (error) {
        console.log("enquiry whatsapp integration error:", error);
    }
    billPopup.value = 'false';
    customerData.value.current_owner = '';
    customerData.value.owner_mobile_no = '';
    customerData.value.whatsappChecked = false;
    customerData.value.callChecked = false;
    customerData.value.smsChecked = false;
    items.value = [];
    serviceDetails.value = [];
    selectedBrand.value = '';
    selectedVariant.value = '';
    quantity.value = '';
    type.value = '';
    pattern.value = '';
}

const searchMobile = ref('')
const boolDetails = reactive({
    state: 0,
});
const mobileSearch = ref(false);
const leadMobile = ref(false);
const handleSearch = async () => {
    if (searchMobile.value) {
        const response = await axios.get(`${BaseURL}/api/method/tyre.api.lead_details`, {
            params: {
                data: searchMobile.value
            },
            headers: headers
        });
        console.log("lead details search", response);
        if (response && response.data.message.message == 'Lead Not Found') {
            showNewCustomer.value = false;
            showAlerts.value = true;
            leadMobile.value = true;
            setTimeout(() => {
                showNewCustomer.value = true;
                showAlerts.value = false;
                leadMobile.value = false;
                searchMobile.value = ""
                leadDetails.value = ""
            }, 1000);
            return;
        }
        else if (response && response.data.message) {
            leadDetails.value = response.data.message;
            boolDetails.state = 1;
            mobileSearch.value = true;
            searchMobile.value = ""
        }

    }
    else {
        showNewCustomer.value = false;
        showAlerts.value = true;
        searchValue.value = true;
        setTimeout(() => {
            showAlerts.value = false;
            searchValue.value = false;
            showNewCustomer.value = true;
        }, 1000);
    }
}
const okCustomer = async () => {
    const data = {
        mobile_no: leadDetails.value.mobile_no,
    };
    console.log("before whatsapp integration enquiry", data.mobile_no)
    try {
        const response = await axios.post(`${BaseURL}/api/method/tyre.api.send_quotation`, { data: JSON.stringify(data) }, { headers: headers })
        console.log("enquiry whatsapp integration success:", response);
    } catch (error) {
        console.log("enquiry whatsapp integration error:", error);
    }
    setTimeout(() => {
        leadDetails.value = '';
        boolDetails.state = 0;
        mobileSearch.value = false;
        searchMobile.value = ''
    }, 1000);
}

const searchMobileAfterResponse = ref(true);
const afterResponse = ref(false);
const enquiryPage = ref(true);
const handleEnquiry = async () => {
    if (!handle.value) {
        enquiryPage.value = true;
        searchMobileAfterResponse.value = true;
        try {
            const response = await axios.get(`${BaseURL}/api/method/tyre.api.stock_details`);
            responseTyreData.value = response.data;
        } catch (error) {
            console.log('Error fetching tyre data:', error);
        }
    }
    else {
        searchMobileAfterResponse.value = false;
        handle.value = false;
        hasResponse.value = false;
        enquiryPage.value = false;
    }
};
onMounted(handleEnquiry)

const clearVehicleData = () => {
    Object.keys(vehicleData.value).forEach(key => {
        vehicleData.value[key] = '';
    });
};

const returnSearch = async (search) => {
    const data = {
        "license_plate": search
    };
    try {
        if (data.license_plate.trim() !== "") {
            const response = await axios.post(`${BaseURL}/api/method/tyre.api.get_details`, { license_plate: JSON.stringify(data.license_plate) }, { headers: headers });
            check.value = true;
            if (response.data.message === "") {
                hasResponse.value = true;
                initial.value = true;
                check.value = false;
                initialNext.value = false;
                return
            } else if (response.data.message === "Enter a Valid vehicle number") {
                if (showNewVehicle.value) {
                    showNewVehicle.value = false;
                    showAlerts.value = true;
                    noValidVehicleNumber.value = true;
                    setTimeout(() => {
                        showAlerts.value = false;
                        noValidVehicleNumber.value = false;
                        showNewVehicle.value = true
                    }, 1000);
                } else if (showNewCustomer.value) {
                    showNewCustomer.value = false;
                    showAlerts.value = true;
                    noCustomerValidVehicleNumber.value = true;
                    setTimeout(() => {
                        showAlerts.value = false;
                        noCustomerValidVehicleNumber.value = false;
                        showNewCustomer.value = true;
                    }, 1000);
                }
                return response.data.message;
            }
            else {
                initial.value = false
                initialNext.value = true
                console.log("response", response.data.message)
                return dataAssignment(response)
            }
        } else {
            showNewCustomer.value = false;
            showAlerts.value = true;
            noVehicleNumber.value = true;
        }
    } catch (error) {
        console.error("Error:", error);
    }
};

const removeCustomerData = () => {
    Object.keys(customerData.value).forEach(key => {
        customerData.value[key] = '';
    });
    employees.value = [{ name: '', type: '' }];
}

const removeEmployee2 = (index) => {
    const data = {
        "current_driver": responseData.value.message[1].current_driver[index].current_driver,
        "parentfield": responseData.value.message[1].current_driver[index].parentfield,
        "mobile_no": responseData.value.message[1].current_driver[index].mobile_no,
        "name": responseData.value.message[1].current_driver[index].parent
    }
    if (data) {
        axios.post(`${BaseURL}/api/method/tyre.api.delete_modified_customers`, { data: data }, { headers: headers });
        responseData.value.message[1].current_driver.splice(index, 1);
    } else {
        console.log(error);
    }
};
const removeEmployee3 = (index) => {
    const data = {
        "contact_person_name": responseData.value.message[1].contact_person[index].contact_person_name,
        "parentfield": responseData.value.message[1].contact_person[index].parentfield,
        "contact_person_mobile": responseData.value.message[1].contact_person[index].contact_person_mobile,
        "name": responseData.value.message[1].contact_person[index].parent
    }
    if (data) {
        axios.post(`${BaseURL}/api/method/tyre.api.delete_modified_customers`, { data: data }, { headers: headers });
        responseData.value.message[1].contact_person.splice(index, 1);
    } else {
        console.log(error);
    }
};
const removeEmployee1 = (index) => {
    // if (sample22.value != 0) {
    employees.value.splice(index, 1);
    // setPrimary();
    // }
};

const deleteVehicle = () => {
    showDeleteConfirmation.value = true;
}
const deleteConfirmation = ref(false);
const confirmDelete = async (vehicle) => {
    const data = {
        name: vehicle
    };
    showDeleteConfirmation.value = false;
    try {
        const response = await axios.post(`${BaseURL}/api/method/tyre.api.delete_vehicle`, { data: JSON.stringify(data) }, { headers: headers })
        if (response.data.message == "deleted") {
            responseData.value = '';
            nextButtonEnable.value = false;
            showAlerts.value = true;
            deleteConfirmation.value = true;
            setTimeout(() => {
                showAlerts.value = false;
                deleteConfirmation.value = false;
            }, 2000);
            returnSearch(vehicle)
        }
    } catch (error) {
        console.log("Vehicle delete error:", error)
    }
}
const cancelDelete = () => {
    showDeleteConfirmation.value = false;
}


//==========================================================>>> 5 point checkup <<<==========================================================================//

const tyreDatas = ref([{ tyre: '', depth: '', pressure: '', comment: '', wear: false, cut: false, mark: false, damage: false, bulge: false, puncture: false, mandatory: false }]);

const sampleValue = reactive({
    index: ref(1),
})

const addTyre = () => {
    if (sampleValue.index < 5) {
        tyreDatas.value.push({ tyre: '', depth: '', pressure: '', comment: '', wear: false, cut: false, mark: false, damage: false, bulge: false, puncture: false });
        sampleValue.index++;
    }
};


const updateTyreData = (index) => {
    const tyre = tyreDatas.value[index];
};

const deleteTyre = (index) => {
    if (sampleValue.index > 1) {
        tyreDatas.value.splice(index, 1);
        sampleValue.index--;
    }
};

const clearData = (index) => {
    const tyre = tyreDatas.value[index];
    tyre.tyre = '';
    tyre.depth = '';
    tyre.pressure = '';
    tyre.comment = '';
    tyre.wear = false;
    tyre.cut = false;
    tyre.mark = false;
    tyre.damage = false;
    tyre.bulge = false;
    tyre.puncture = false;
    tyre.mandatory = false;
};

//========================================================>>> Required Services <<<============================================================================//

let selectedCheckbox = ref(null);

const show = ref({
    Ac: false,
    battery: false,
    wiper: false,
    car_wash: false,
    alignment: false,
    rotation: false,
    oil_change: false,
    balancing: false,
    inflation: false,
    inflation_air: false,
    inflation_nitrogen: false,
    ac_service_checkbox: false,
    battery_service_checkbox: false,
    wiper_service_checkbox: false,
    car_wash_service_checkbox: false,
    alignment_service_checkbox: false,
    rotation_service_checkbox: false,
    oil_change_service_checkbox: false,
    balancing_service_checkbox: false,
    inflation_service_checkbox: false,
    puncture_checkbox: false,
    tyre_edge_checkbox: false,
    tyre_path_checkbox: false,
    mushroom_path_checkbox: false
})

function handleCheckboxChange(checkboxId) {
    if (selectedCheckbox.value === checkboxId) {
        selectedCheckbox.value = null;
    } else {
        selectedCheckbox.value = checkboxId;
        const otherCheckboxId = checkboxId === 'air' ? 'nitrogen' : 'air';
        requireService.value.inflations.type = selectedCheckbox.value;
        const otherCheckbox = document.getElementById(otherCheckboxId);
        if (otherCheckbox) {
            otherCheckbox.checked = false;
            if (otherCheckboxId == 'air') {
                show.value.inflation_air = false;
                show.value.inflation_nitrogen = true;
            }
            else {
                show.value.inflation_air = true;
                show.value.inflation_nitrogen = false;
            }
        }
    }
}
const requireService = ref({
    mandatory: false,
    Alignment: false,
    Rotation: false,
    Oil_change: false,
    Balancing: false,
    Inflation: false,
    AcService: false,
    Battery: false,
    Wiper: false,
    CarWash: false,
    alignments: {
        lastAlignment: '',
        nextAlignment: ''
    },
    rotations: {
        inche: '',
        wheel_count: 1
    },
    oil_changes: {
        oil_quality: '',
        oil_quantity: ''
    },
    balancings: {
        fl: '',
        fr: '',
        bl: '',
        br: '',
        st: '',
        inches: '',
        type: '',
        gramsCheck: false
    },
    inflations: {
        type: '',
        ft: '',
        rt: ''
    },
    // ac: '',
    // battery: '',
    // wiper: '',
    // car_wash: '',
    Puncture: false,
    TyreEdge: false,
    TyrePatch: false,
    MushroomPatch: false,
})
const showGrams = ref(false)
function handleGrams() {
    if (requireService.value.balancings.gramsCheck) {
        showGrams.value = true;
    } else {
        showGrams.value = false
    }
}

function checkup(data) {
    console.log("final data checking in last page", data);
    try {
        const response = axios.post(`${BaseURL}/api/method/tyre.api.job_card`, { data: JSON.stringify(data), brand: responseData.value.message[0].vehicle_brand, model: responseData.value.message[0].vehicle_model }, { headers: headers })
        console.log('job card after response', response);
    } catch (error) {
        console.log("error");
    }
}
function shooo() {
    console.log(requireService.value);
}
function handleShow(item) {
    switch (item) {
        case 'ac_service':
            show.value.Ac = !show.value.Ac;
            requireService.value.AcService = show.value.Ac;
            if (show.value.Ac == false) {
                requireService.value.Ac = '';
            }
            break;
        case 'battery':
            show.value.battery = !show.value.battery;
            requireService.value.Battery = show.value.battery;
            if (show.value.battery == false) {
                requireService.value.Battery = '';
            }
            break;
        case 'wiper':
            show.value.wiper = !show.value.wiper;
            requireService.value.Wiper = show.value.wiper;
            if (show.value.wiper == false) {
                requireService.value.Wiper = '';
            }
            break;
        case 'car_wash':
            show.value.car_wash = !show.value.car_wash;
            requireService.value.CarWash = show.value.car_wash;
            if (show.value.car_wash == false) {
                requireService.value.CarWash = '';
            }
            break;
        case 'alignment':
            show.value.alignment = !show.value.alignment;
            requireService.value.Alignment = show.value.alignment;
            if (show.value.alignment == false) {
                requireService.value.alignments.lastAlignment = '';
                requireService.value.alignments.nextAlignment = '';
            }
            break;
        case 'rotation':
            show.value.rotation = !show.value.rotation;
            requireService.value.Rotation = show.value.rotation;
            if (show.value.rotation == false) {
                requireService.value.rotations.inche = '';
                requireService.value.rotations.wheel_count = 1;
            }
            break;
        case 'oil_change':
            show.value.oil_change = !show.value.oil_change;
            requireService.value.Oil_change = show.value.oil_change;
            if (show.value.oil_change == false) {
                requireService.value.oil_changes.oil_quality = '';
                requireService.value.oil_changes.oil_quantity = '';
            }
            break;
        case 'balancing':
            show.value.balancing = !show.value.balancing;
            requireService.value.Balancing = show.value.balancing;
            if (show.value.balancing == false) {
                requireService.value.balancings.inches = '';
                requireService.value.balancings.type = '';
                requireService.value.balancings.gramsCheck = false;
                requireService.value.balancings.fl = '';
                requireService.value.balancings.fr = '';
                requireService.value.balancings.bl = '';
                requireService.value.balancings.br = '';
                requireService.value.balancings.st = '';
                showGrams.value = false;
            }
            break;
        case 'inflation':
            show.value.inflation = !show.value.inflation;
            requireService.value.Inflation = show.value.inflation;
            if (show.value.inflation == false) {
                requireService.value.inflations.type = '';
                requireService.value.inflations.ft = '';
                requireService.value.inflations.rt = '';
                show.value.inflation_air = false;
                show.value.inflation_nitrogen = false;
            }
            break;
    }
}
function handelCheck(data) {
    switch (data) {
        case 'puncture':
            show.puncture_checkbox = !show.puncture_checkbox;
            if (show.puncture_checkbox == true) {
                requireService.value.Puncture = true;
            } else {
                requireService.value.Puncture = false;
            }
            break
        case 'tyre_edge':
            show.tyre_edge_checkbox = !show.tyre_edge_checkbox;
            if (show.tyre_edge_checkbox == true) {
                requireService.value.TyreEdge = true;
            } else {
                requireService.value.TyreEdge = false;
            }
            break;
        case 'tyre_patch':
            show.tyre_path_checkbox = !show.tyre_path_checkbox;
            if (show.tyre_path_checkbox == true) {
                requireService.value.TyrePatch = true;
            } else {
                requireService.value.TyrePatch = false;
            }
            break;
        case 'mushroom_patch':
            show.mushroom_path_checkbox = !show.mushroom_path_checkbox;
            if (show.mushroom_path_checkbox == true) {
                requireService.value.MushroomPatch = true;
            } else {
                requireService.value.MushroomPatch = false;
            }
            break;
    }
}

// function get_itemrate(data,index){
//     console.log("data",data)
//     console.log("index",index)
//     console.log(tableData.value);
//     let amount=getrate(data)
//     console.log("rate",amount.value);
//     console.log(tableData.value[index][0].itemCode)
//     tableData.value[index][0].rate=getrate(data);
//     console.log(tableData.value);
//     // print(tableData)
// }

// async function getrate(data) {
//     let rate = 0
//     console.log(data)
//     try {
//         // Assuming headers is defined elsewhere
//         const response = await axios.get(`${BaseURL}/api/method/tyre.api.get_item_rate`, {
//             params: { item_code: data },
//             headers: headers // Assuming headers is defined elsewhere
//         }).then((response) => {
//             rate = response.data.message
//             console.log(rate, "rate - bhavan");
//         })
//         console.log(rate)
//         return rate;
//     } catch (error) {
//         console.error("Error:", error);
//         throw error; // Rethrow the error to be caught by the caller
//     }
// }

async function get_itemrate(data, index) {
    console.log("======================data========================", data);
    console.log("index", index);
    console.log(tableData.value);

    try {
        let rate = await getrate(data); // Wait for getrate() to complete and get the rate
        console.log("rate", rate);
        console.log(tableData.value[index][0].itemCode);
        tableData.value[index][0].rate = rate; // Set the rate in the tableData
        console.log(tableData.value);
    } catch (error) {
        console.error("Error:", error);
        // Handle the error as needed
    }
}

async function getrate(data) {
    let inch = ''
    let type = ''
    if (data === "Rotation") {
        console.log("+++++++++++++++++++yes++++++++++++++++++")
        inch = requireService.value.rotations.inche;
    }
    else if (data === "Balancing") {
        type = requireService.value.balancings.type;
        inch = requireService.value.balancings.inches;
    }
    else {
        inch = ''
    }
    try {
        const response = await axios.get(`${BaseURL}/api/method/tyre.api.get_item_rate`, {
            params: { item_code: data, brand: responseData.value.message[0].vehicle_brand, model: responseData.value.message[0].vehicle_model, inch: inch, type: type },
            headers: headers // Assuming headers is defined elsewhere
        });
        const rate = response.data.message;
        console.log(rate, "rate - bhavan");
        return rate;
    } catch (error) {
        console.error("Error:", error);
        throw error; // Rethrow the error to be caught by the caller
    }
}


//===================================================>>> Replacement Tyre Details <<<========================================================================//

const maxYears = ref(0)
const tyrePositions = ['Front Left', 'Front Right', 'Rear Left', 'Rear Right', 'Spare'];
const replace = reactive({
    target: false
});
let billIndex = 0;
const warrantyYears = (warranty) => {
    const today = new Date();
    const expiryDate = new Date(today.getFullYear() + parseFloat(warranty), today.getMonth(), today.getDate());
    const month = expiryDate.getMonth() + 1; // Adding 1 because getMonth() returns zero-based index
    const day = expiryDate.getDate();
    const year = expiryDate.getFullYear();
    maxYears.value = `${month}_${day}_${year}`;
    const sendYears = `${year}-${month}-${day}`; // Formatting as 'YYYY-MM-DD'
    console.log('send years ', sendYears);
    if (!warranty) {
        maxYears.value = 0;
    }
    return sendYears;
}
function formatValue(value, type) {
    if (value === 0 || value === undefined || value === null) {
        return 'Nill';
    }
    return type === 'warranty' ? `${value} years` : `${value}`;
}
const additional = (additional) => {
    return additional ? ' (additonal sale)' : ''
}
const tyres = ref([{
    type: '',
    loadIndex: '',
    brand: '',
    speedRating: '',
    pattern: '',
    size: '',
    ttTl: '',
    item: '',
    rate: '',
    warranty: '',
    maxYears: warrantyYears(0),
    mandatory: false,
    status: false,
}]);
watchEffect(() => {
    tyres.value.forEach(tyre => {
        tyre.maxYears = warrantyYears(tyre.warranty);
    });
});

const size = ref([])
const saveData = (index) => {
    console.log(resData.value);
    console.log(tyres.value);
    console.log(tyres.value[index].brand);
};

const setValue = reactive({
    index: ref(1)
});

const addTyreReplacement = () => {
    if (setValue.index < 5) {
        tyres.value.push({
            loadIndex: '',
            brand: '',
            speedRating: '',
            pattern: '',
            size: '',
            ttTl: '',
            item: '',
            rate: '',
            warranty: '',
            status: false
        })
        setValue.index++;
        replace.target = false;
    }
}
const deleteTyreReplacement = (index) => {
    if (setValue.index > 1) {
        tyres.value.splice(index, 1)
        setValue.index--;
    }
}
const clearTyreData = (index) => {
    const tyre = tyres.value[index]
    tyre.type = '';
    tyre.loadIndex = '';
    tyre.brand = '';
    tyre.speedRating = '';
    tyre.pattern = '';
    tyre.size = '';
    tyre.ttTl = '';
    tyre.rate = '';
    tyre.item = '';
    tyre.warranty = '',
        tyre.mandatory = false;
    tyre.status = false;
};
let step = 0;
const tableData = ref([]);
function addValue(data, replace) {
    // Check if data is an array
    console.log('addvalue function data-type', typeof data);

    console.log('addvalue function data', data);
    if (Array.isArray(data)) {
        console.log(replace.target, "UIO");
        // Data is a list (array)
        if (!replace.target) {
            data.forEach(item => {
                console.log(item);
                console.log('is this addvalue parameter data?', item.item);

                let existingItemIndex = -1;
                //check if add a new data
                console.log(item.status, "status")
                if (existingItemIndex === -1 && !item.status) {
                    // If item is not found and not already processed, add it to tableData
                    console.log(billIndex, "billIndex-N")


                    let newOne = true;
                    // Check if tableData.value[billIndex] is an array
                    if (Array.isArray(tableData.value)) {
                        for (let index = 0; index < tableData.value.length; index++) {
                            const rowData = tableData.value[index];
                            console.log(rowData, "Array")
                            for (let i = 0; i < rowData.length; i++) {
                                const items = rowData[i];
                                if (items.itemCode === item.item) {
                                    // Item already exists, update quantity and mark as processed
                                    console.log(items.requiredQuantity, "exist")
                                    items.requiredQuantity++;
                                    console.log(items.requiredQuantity)
                                    item.status = true;
                                    existingItemIndex = index;
                                    break;
                                }
                            }
                            if (existingItemIndex > -1) {
                                console.log(existingItemIndex, "EI")
                                newOne = false;
                                break;
                            }
                        }
                    }

                    // Create a new object for the item
                    console.log(existingItemIndex, "EO");
                    if (existingItemIndex < 0) {
                        const newData = {
                            itemCode: item.item,
                            sourceWarehouse: '',
                            rate: item.rate,
                            warranty: item.warranty,
                            requiredQuantity: 1, // Set initial quantity to 1
                            cost: ''
                        };

                        // Push the new object into the array at the specified billIndex
                        console.log(newData, "newData")
                        console.log(billIndex, "push")
                        if (newData.itemCode) {
                            if (!Array.isArray(tableData.value[billIndex])) {
                                tableData.value[billIndex] = [];
                            }

                            tableData.value[billIndex].push(newData);

                            // Mark the item as processed
                            item.status = true;
                            billIndex++;
                        }
                        console.log(billIndex, "After-Push")

                    }
                }

                calculateTotals();
                // billIndex++;
            });
        }

        // If the current step is 3, empty the tableData
        // if (step === 3) {
        //     console.log("hiiii")
        //     tableData.value = [];
        // }
        console.log(tableData.value.itemCode);
        console.log(billIndex)
        console.log(tableData[billIndex], "new");

        // replace.target = true;
        console.log(billIndex, "Total")
    }
    else if (typeof data === 'object') {
        for (const key in data) {
            // console.log(Object.hasOwnProperty.call(data, key),"object")
            if (Object.hasOwnProperty.call(data, key)) {
                console.log("key checking", data[key])
                if (data[key] == true) {
                    let itemExists = false;
                    tableData.value.forEach((rowData, index) => {
                        rowData.forEach(item => {
                            console.log("step 2: itemcode in billing page for tyre 11", item.itemCode)
                            if (item.itemCode === key) {
                                console.log("step 3:itemcode in billing page for tyre 22", item.itemCode)
                                itemExists = true;
                                getrate(key).then(rate => {
                                    item.rate = rate;
                                })
                            }
                        });
                    });
                    if (!itemExists) {
                        const newData = {
                            itemCode: key,
                            sourceWarehouse: '',
                            warranty: 0,
                            requiredQuantity: 1,
                            cost: ''
                        };
                        console.log("==============", key, "********************")
                        getrate(key).then(rate => {
                            if (key === "Rotation") {
                                newData.requiredQuantity = requireService.value.rotations.wheel_count;
                            }
                            console.log(newData, "----------------------------------")
                            newData.rate = rate
                            console.log(newData.rate)
                        }).catch(error => {
                            console.error("Error:", error);
                        });
                        console.log(billIndex, "before")
                        if (!Array.isArray(tableData.value[billIndex])) {
                            console.log("hello")
                            tableData.value[billIndex] = [];
                        }

                        tableData.value[billIndex].push(newData);
                        calculateTotals();

                        billIndex++;
                    }
                }
                else {
                    console.log("hi this is else block")
                }
            }
        }
    }
    // Update the step variable
    step = billIndex;
}
//===================================================>>> Billing Details <<<=========================================================================================//

const totalRate = ref(0);
const totalQuantity = ref(0);
const totalCost = ref(0);
const discountRate = ref();
const finalAmount = ref();

const calculateTotals = () => {
    let sumRate = 0;
    let sumQuantity = 0;
    let sumCost = 0;

    console.log(tableData.value, "tableData.value")
    tableData.value.forEach(row => {
        // Assuming each row is an object
        console.log(row, "row")
        const rate = parseFloat(row[0].rate) || 0;
        const quantity = parseFloat(row[0].requiredQuantity) || 0;
        row[0].cost = (rate * quantity).toFixed(2);
        sumRate += rate;
        sumQuantity += quantity;
        sumCost += rate * quantity;
    });

    totalRate.value = sumRate;
    totalQuantity.value = sumQuantity;
    totalCost.value = sumCost;
    finalAmount.value = sumCost;
};
const calculateDiscountRate = () => {
    if (discountRate.value == 0) {
        finalAmount.value = totalCost.value;
        return
    }
    finalAmount.value = totalCost.value - discountRate.value;
};

const addNewRow = (billIndex) => {
    // Check if tableData[billIndex] is defined and is an array
    console.log(billIndex)
    console.log(step)
    if (!Array.isArray(tableData.value[step])) {
        tableData.value[step] = [];
    }
    // Push a new object into tableData[billIndex]
    tableData.value[step].push({
        itemCode: '',
        sourceWarehouse: '',
        rate: '',
        requiredQuantity: 0,
        cost: '',
        additional: 'additional'
    });
    console.log(tableData.value[step])
    step++;
    billIndex = step
};

const removeRow = (index) => {
    tableData.value.splice(index, 1);
    step--;
    billIndex = step;
    calculateTotals();
};
const showConfirm = ref(false)
const dataFinalSubmission = () => {
    showConfirm.value = true;
}
const finalSuccess = ref(false);
const confirmDataSave = async () => {
    showConfirm.value = false;
    jobCard["bill"] = tableData.value
    checkup(jobCard)
    finalSuccess.value = true;
    enquiryPage.value = true;
    setTimeout(async () => {
        const data = {
            mobile_no: responseData.value.message[1]?.owner_mobile_no,
            license_plate: responseData.value.message[0]?.name
        };
        console.log("before whatsapp integration", data.mobile_no)
        console.log("before whatsapp integration", data.license_plate)
        try {
            const response = await axios.post(`${BaseURL}/api/method/tyre.api.send_quotation`, { data: JSON.stringify(data) }, { headers: headers })
            console.log("whatsapp integration success:", response);
        } catch (error) {
            console.log("whatsapp integration error:", error);
        }
        finalSuccess.value = false;
        currentstep.value = 0;
        check.value = false;
        initialNext.value = false;
        hasResponse.value = true;
        initial.value = true;
        responseData.value = '';
        nextButtonEnable.value = false;
        afterResponse.value = false;
        handle.value = false
        searchMobileAfterResponse.value = true
        //     if (tyreDatas.value[key] == Boolean) {
        //         tyreDatas.value[key] = false;
        //     }
        //     else {
        //         tyreDatas.value[key] = '';
        //     }
        // })
        // tyres.value.forEach(tyre => {
        //     for (let key in tyre) {
        //         tyre[key] = '';
        //     }
        //     tyre.maxYears = warrantyYears(0);
        //     tyre.mandatory = false;
        //     tyre.status = false;
        // });
        // // Loop through each property of the object
        // for (let key in requireService.value) {
        //     // If the property value is an object, loop through its properties
        //     if (typeof requireService.value[key] === 'object') {
        //         for (let innerKey in requireService.value[key]) {
        //             // Set sub-properties to empty strings
        //             requireService.value[key][innerKey] = '';
        //         }
        //     } else {
        //         // Set properties to false
        //         requireService.value[key] = false;
        //     }
        // }

        // // Set sub-properties of the show object to false
        // show.alignment.value = false;
        // show.rotation.value = false;
        // show.oil_change.value = false;
        // show.inflation.value = false;
        // show.balancing.value = false;
        // window.location.reload()
    }, 1000);
}
const cancelSaved = () => {
    showConfirm.value = false;
}
</script>

<style scoped>
.dark-hr {
    height: 2px;
    background-color: #000000 !important;
}

.bottom-div {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #f0f0f0;
}

.active {
    font-weight: bold;
}

.person-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.custom-dropdown {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-top: 1rem;
    width: 20%;
    /* Set width here instead of in the input */
}

.custom-input {
    width: 100%;
    /* Input takes full width of the parent */
    box-sizing: border-box;
    /* Include padding and border in the element's total width */
}

.custom-dropdown-list {
    display: none;
    /* Hide dropdown list by default */
    width: 100%;
    /* Full width of the parent */
    max-height: 150px;
    overflow-y: auto;
    background-color: #fff;
    border: 1px solid #ccc;
    border-top: none;
    list-style-type: none;
    padding: 0;
    border-radius: 0.75rem;
    margin: 0;
}

.custom-dropdown-item {
    padding: 10px;
    cursor: pointer;
}

.custom-dropdown-item:hover {
    background-color: #f0f0f0;
}

.custom-dropdown:hover .custom-dropdown-list {
    display: block;
    /* Show dropdown list on hover */
}
</style>
