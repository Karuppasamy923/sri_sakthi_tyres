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
                <h1 class="text-[20px] font-bold mb-6">Welcome User 1</h1>
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
                                    <button @click="confirmCustomerSave" v-if="newCustomerSave"
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
                                    <div class="flex justify-end">
                                        <button @click="billPopup = 'false'">
                                            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                                                fill="none" viewBox="0 0 14 14">
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
                                                    Brand
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Size
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Quantity
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Type
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Pattern
                                                </th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                                                v-for="(item, index) in items" :key="index">
                                                <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                                                    scope="row">{{ item.brand }}</td>
                                                <td class="px-6 py-4">{{ item.size }}</td>
                                                <td class="px-6 py-4">{{ item.quantity }}</td>
                                                <td class="px-6 py-4">{{ item.quantity }}</td>
                                                <td class="px-6 py-4">{{ item.type }}</td>
                                                <td class="px-6 py-4">{{ item.pattern }}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </a>
                        </div>
                        <div v-if="jobCardPopup == 'true'"
                            class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-center items-center">
                            <a href="#"
                                class="block max-w-[70rem] p-10 pt-5 bg-white border border-gray-200 rounded-lg shadow">
                                <div class="grid grid-cols-2">
                                    <div>
                                        <h5 class="mb-2 text-2xl font-bold tracking-tight text-black">
                                            Price Details</h5>
                                    </div>
                                    <div class="flex justify-end">
                                        <button @click="jobCardPopup = 'false'">
                                            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                                                fill="none" viewBox="0 0 14 14">
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
                                                    Brand
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Size
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Quantity
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Type
                                                </th>
                                                <th scope="col" class="px-6 py-3">
                                                    Pattern
                                                </th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                                                v-for="(item, index) in items" :key="index">
                                                <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                                                    scope="row">{{ item.brand }}</td>
                                                <td class="px-6 py-4">{{ item.size }}</td>
                                                <td class="px-6 py-4">{{ item.quantity }}</td>
                                                <td class="px-6 py-4">{{ item.quantity }}</td>
                                                <td class="px-6 py-4">{{ item.type }}</td>
                                                <td class="px-6 py-4">{{ item.pattern }}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </a>
                        </div>




                        <div v-if="showWarning"
                            class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-center items-center">
                            <div class="bg-white rounded-lg p-8 shadow-xl">
                                <p class="mb-4">Please fill the required fields</p>
                                <div class="flex justify-center">
                                    <button @click="close"
                                        class="bg-red-500 text-white font-semibold px-4 py-2 rounded mr-2">Ok</button>
                                </div>
                            </div>
                        </div>

                    <!-- </div> -->
                    <div v-if="showAlerts"
                        class="fixed inset-0 overflow-hidden bg-black bg-opacity-50 flex justify-center items-center">
                        <div class="bg-white rounded-lg p-8 shadow-xl">
                            <p class="mb-4" v-if="vehicleNumber">Please fill the required fields!</p>
                            <p class="mb-4" v-if="searchValue">Please fill the search value!</p>
                            <p class="mb-4 text-red-500" v-if="wrongSearchValue">Enter valid Vehicle Number!</p>
                            <p class="mb-4" v-if="vehicleExist">Vehicle already exists!</p>
                            <p class="mb-4 text-green-500" v-if="successData">Details added successfully!</p>
                            <p class="mb-4 text-green-500" v-if="modifyAlert">Successfully modified vehicle data!</p>
                            <p class="mb-4" v-if="notVehicleAlert">Vehicle not exists!</p>
                            <p class="mb-4" v-if="noVehicleNumber">Enter vehicle number!</p>
                            <p class="mb-4" v-if="noValidVehicleNumber">Enter valid vehicle number!</p>
                            <p class="mb-4" v-if="noCustomerValidVehicleNumber">Enter valid vehicle number!</p>
                            <p class="mb-4" v-if="notCustomerAlert">Please fill the Customer details!</p>
                            <p class="mb-4" v-if="notEmployeeAlert">Please add atleast one Employee!</p>
                            <p class="mb-4" v-if="notEmpDetailAlert">Please fill required Employee details!</p>
                            <p class="mb-4 text-green-500" v-if="deleteConfirmation">Vehicle details deleted
                                successfully!</p>
                            <p class="mb-4 text-red-500 font-bold" v-if="cannotSave">! It's a search details. Can't
                                save..</p>
                            <p class="mb-4 text-red-500 font-bold" v-if="customerExist">! Customer already added to this
                                vehicle..</p>
                            <div class="flex justify-center">
                                <button @click="closed"
                                    v-if="vehicleNumber || vehicleExist || notCustomerAlert || notEmployeeAlert || notEmpDetailAlert || notVehicleAlert || noVehicleNumber || noValidVehicleNumber || noCustomerValidVehicleNumber"
                                    class="bg-red-500 text-white font-semibold px-4 py-2 rounded mr-2">Ok</button>
                                <button @click="close" v-if="successData || modifyAlert || searchValue"
                                    class="bg-green-500 text-white font-semibold px-4 py-2 rounded mr-2">Ok</button>

                            </div>
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
                    <!-- <div v-if="currentstep == 0"> -->
                        <div class="flex justify-center m-5">
                            <input type="text" class="w-[338px] h-[52px] rounded-sm border-solid border border-black"
                                v-model="searchQuery" @keyup.enter="search" placeholder="Enter Vehicle Number">
                            <button class="bg-blue-500 w-[150px] text-white font-bold text-base p-4 rounded-lg ml-3"
                                @click="search">Search</button>
                        </div>
                        <div class="grid grid-cols-2 gap-3" v-if="responseData && responseData.message && check">
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
                                                <label>Chassis No&nbsp;&nbsp;:&nbsp; </label>
                                                <label class="mt-3">{{ responseData && responseData.message &&
                                                    responseData.message[0]?.chassis_no
                                                    || 'No data' }}</label>
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
                                            <!-- <div v-for="(employee, index) in responseData.message[1]?.current_driver"
                                                :key="index"> -->
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
                                            <!-- </div> -->
                                            <!-- <div v-for="(contact, index) in responseData.message[1]?.contact_person"
                                                :key="index"> -->
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
                                            <!-- </div> -->
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
                                            <!-- <div v-for="(employee, index) in responseData.message[1]?.current_driver"
                                                :key="index"> -->
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
                                            <!-- </div> -->
                                            <!-- <div v-for="(contact, index) in responseData.message[1]?.contact_person"
                                                :key="index"> -->
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
                                            <!-- </div> -->

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
                        <div v-if="hasResponse && initial">
                            <div class="flex">
                                <div class="mr-8">
                                    <button @click="getJobCard" v-if="hide == 'false' && hideEnq == 'false'"
                                        class="bg-blue-500 w-[100px] text-white font-bold p-2 rounded-lg mt-4 mb-4">Job
                                        Card</button>
                                    <button @click="hide = 'false'" v-if="hide != 'false'"
                                        class="bg-blue-500 w-[100px] text-white font-bold p-2 rounded-lg mt-4 mb-4">Back</button>
                                </div>
                                <div>
                                    <button @click="getEnquiry" v-if="hideEnq == 'false' && hide == 'false'"
                                        class="bg-blue-500 w-[100px] text-white font-bold p-2 rounded-lg mt-4 mb-4">Enquiry</button>
                                    <button @click="hideEnq = 'false'" v-if="hideEnq != 'false'"
                                        class="bg-blue-500 w-[100px] text-white font-bold p-2 rounded-lg mt-4 mb-4">Back</button>
                                </div>
                                <div>
                                    <Input type="number" placeholder="search ..." v-if="hideEnq != 'false'"
                                        v-model="searchEnquiry" @input="getEnquiry" class="mt-9 mb-2 -ml-14.5 p-4" />
                                    <Input placeholder="Vehicle Search ..." v-if="hide != 'false'"
                                        v-model="searchJobCard" @input="getJobCard" class="mt-9 mb-2 -ml-14.5 p-4" />
                                </div>
                            </div>
                            <div>
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
                                                v-for="jobcard in jobCardDetails" :key="jobcard">
                                                <th scope="row"
                                                    class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-black">
                                                    <a href="#" @click="fetchJobCard(jobcard.name)">{{ jobcard.name
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
                            <div>
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
                            <div class="flex justify-center" v-if="hide == 'false' && hideEnq == 'false'">
                                <div class="flex justify-center mt-9">
                                    <img src="https://img.freepik.com/free-vector/hand-drawn-no-data-concept_52683-127823.jpg?w=996&t=st=1712321166~exp=1712321766~hmac=ae2f4e19eb0e1185d52ac8a07c158e9dc5afa741284e9526a8e8a0165573735b"
                                        alt="No data" class="w-[25%]" @click="showMessage">
                                </div>
                            </div>
                            <div class="flex justify-center m-5" v-if="hide == 'false'">
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

                                    <p class="m-2">Chassis No <span class="text-red-500 font-bold">*</span><br>

                                        <input type="text"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.chassis_no" placeholder="Enter Chassis No">
                                    </p>
                                    <p class="m-2">Fuel Type <span class="text-red-500 font-bold">*</span><br>
                                        <select v-model="vehicleData.fuel_type"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black">
                                            <option value="" disabled selected>Select fuel type...</option>
                                            <option value="Petrol">Petrol</option>
                                            <option value="Diesel">Diesel</option>
                                            <option value="EV">EV</option>
                                            <option value="hybrid ">Hybrid</option>
                                        </select>
                                    </p>
                                    <p class="m-2">Odometer reading (kms) <span class="text-red-500 font-bold">*</span><br>
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
                                        <input type="text" v-if="check"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="responseData.message[0].vehicle_brand"
                                            placeholder="Enter Vehicle Brand">
                                    </p>
                                    <p class="m-2">Vehicle Model <br>
                                        <input type="text" v-if="check"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="responseData.message[0].vehicle_model"
                                            placeholder="Enter Vehicle Model">
                                    </p>
                                    <p class="m-2">Chassis No <br>
                                        <input type="text" v-if="check"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="responseData.message[0].chassis_no" placeholder="Enter Chassis No">
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
                                    <div class="pb-4 grid grid-cols-2 ml-24" v-if="hasResponse">
                                        <input type="tel" v-model="searchMobile"
                                            class="w-[19rem] h-[3rem] mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter Customer Mobile No.">
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
                                        <input type="text"  v-model="responseData.message[0].name"
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
                                    <input type="checkbox" v-model="customerData.whatsappChecked"
                                        :checked="leadDetails.custom_whatsapp == '1'" :disabled="boolDetails.state == 1"
                                        class="bg-gray-300 rounded-sm">&nbsp;&nbsp; <label>WhatsApp</label>
                                    <span class="ml-5">
                                        <input type="checkbox" v-model="customerData.callChecked"
                                            :checked="leadDetails.custom_whatsapp == '1'"
                                            :disabled="boolDetails.state == 1"
                                            class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>call</label>
                                    </span>
                                    <span class="ml-5">
                                        <input type="checkbox" v-model="customerData.smsChecked"
                                            :checked="leadDetails.custom_whatsapp == '1'"
                                            :disabled="boolDetails.state == 1"
                                            class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>SMS</label>
                                    </span>
                                    <div v-if="!handle && !hasResponse">
                                        <div v-for="(employee, index) in employees" :key="index" class="mt-2">
                                            <div v-show="false">{{ sample22 = index }}</div>
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
                                                <select v-model="employee.type" @click="setPrimary(index)"
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
                                    <div v-if="hasResponse">
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
                                                    @change="getType(selectedBrand, selectedVariant, index)">
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
                                                <!-- <label class="mt-2">Add</label> -->
                                                <Button class="w-[4rem] mt-10" @click="addItem">Add</Button>
                                            </div>
                                            <div class="flex flex-col ml-1">
                                                <label class="mt-2">Type</label>
                                                <select
                                                    class="w-[8rem] h-[3rem] rounded-sm border-solid border border-black"
                                                    v-model="type"
                                                    @change="getPattern(selectedBrand, selectedVariant, type, index)">
                                                    <option v-for="(type, index) in types[index]" :key="index">{{ type
                                                        }}</option>
                                                </select>
                                            </div>
                                            <div class="flex flex-col ml-1">
                                                <label class="mt-2">Pattern</label>
                                                <select
                                                    class="w-[8rem] h-[3rem] rounded-sm border-solid border border-black"
                                                    v-model="pattern">
                                                    <option v-for="(pattern, index) in patterns[index]" :key="index">{{
                                                        pattern
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
                                                        <td>{{ item.brand }}</td>
                                                        <td>{{ item.size }}</td>
                                                        <td>{{ item.quantity }}</td>
                                                        <td>{{ item.quantity }}</td>
                                                        <td>{{ item.type }}</td>
                                                        <td>{{ item.pattern }}</td>
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
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm">
                                                <label>Alignment</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.rotation"
                                                    :checked="leadDetails.custom_rotation == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm">
                                                <label>Rotation</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.oil_change"
                                                    :checked="leadDetails.custom_oil_change == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm">
                                                <label>Oil Change</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.balancing"
                                                    :checked="leadDetails.custom_balancing == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm">
                                                <label>Balancing</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.inflation"
                                                    :checked="leadDetails.custom_inflation == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm">
                                                <label>Inflation</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.puncture"
                                                    :checked="leadDetails.custom_puncture == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm">
                                                <label>Puncture</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.tyre_edge"
                                                    :checked="leadDetails.custom_tyre_edge == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm">
                                                <label>Tyre Edge</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.tyre_patch"
                                                    :checked="leadDetails.custom_tyre_edge == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm">
                                                <label>Tyre Patch</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.mushroom_patch"
                                                    :checked="leadDetails.custom_mushroom_patch == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm">
                                                <label>Mushroom Patch</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.ac_service"
                                                    :checked="leadDetails.custom_ac_service == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm">
                                                <label>AC Service</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.battery"
                                                    :checked="leadDetails.custom_battery == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm">
                                                <label>Battery</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.wiper"
                                                    :checked="leadDetails.custom_wiper == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm">
                                                <label>Wiper</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.car_wash"
                                                    :checked="leadDetails.custom_car_wash == '1'"
                                                    :disabled="boolDetails.state == 1" class="bg-gray-300 rounded-sm">
                                                <label>Car Wash</label>
                                            </div>
                                        </div>
                                        <div>
                                            <button
                                                class="bg-green-500 w-[100%]  text-white font-bold 0 text-base p-4 rounded-lg m-3"
                                                @click="handleCustomer">Save</button>
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
                                                    :selected="employee.parentfield === 'contact_person'">Contact Person
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
                                                    :selected="contact.parentfield === 'contact_person'">Contact Person
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
                                    <label class="mt-2" :for="'tyre' + index">Tyre<span
                                            class="text-red-500 font-bold">*</span></label>
                                    <select class="w-[100%] h-[3.5rem] rounded-sm" v-model="tyreData.tyre"
                                        :id="'type' + index" style="border: 1px solid black;"
                                        @change="updateTyreData(index)">
                                        <option value="" selected>Please select...</option>
                                        <option value="Front Left">Front Left</option>
                                        <option value="Front Right">Front Right</option>
                                        <option value="Rear Left">Rear Left</option>
                                        <option value="Rear Right">Rear Right</option>
                                        <option value="Spare Tyre">Spare Tyre</option>
                                    </select>
                                </div>
                                <div class="flex flex-col space-y-1">
                                    <label class="mt-2" :for="'RTD' + index">Remaining Tread Depth</label>
                                    <input v-model="tyreData.depth"
                                        class="w-[100%] h-[3.5rem] rounded-sm border-solid border border-black"
                                        type="text" :id="'RTD' + index" @change="updateTyreData(index)">
                                        <span v-if="tyreData.mandatory && !tyreData.depth.trim()"
                                        class="text-red-500 font-bold">Please fill this required field</span>
                                </div>
                                <div class="flex flex-col space-y-1">
                                    <label class="mt-2" :for="'TP' + index">Tyre Pressure (psi)</label>
                                    <input v-model="tyreData.pressure"
                                        class="w-[100%] h-[3.5rem] rounded-sm border-solid border border-black"
                                        type="text" :id="'TP' + index" @change="updateTyreData(index)">
                                        <span v-if="tyreData.mandatory && !tyreData.pressure.trim()"
                                        class="text-red-500 font-bold">Please fill this required field</span>
                                </div>
                                <div class="flex flex-col space-y-1">
                                    <label class="mt-2" :for="'COM' + index">Comment</label>
                                    <input v-model="tyreData.comment"
                                        class="w-[100%] h-[3.5rem] rounded-sm border-solid border border-black"
                                        type="text" :id="'COM' + index" @change="updateTyreData(index)">
                                        <span v-if="tyreData.mandatory && !tyreData.comment.trim()"
                                        class="text-red-500 font-bold">Please fill this required field</span>
                                </div>
                            </div>
                            <div class="ml-9">
                                <FeatherIcon name="trash-2" class="mt-11 w-8 h-8 cursor-pointer text-red-500"
                                    @click="deleteTyre(index)" />
                            </div>
                        </div>
                        <div class="flex flex-row space-x-20">
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
                                        v-model="show.mushroom_path_checkbox" id="mushroom_batch"
                                        @change="handelCheck('mushroom_patch')">
                                    <label class="text-[18px]" for="mashroom_batch">Mushroom Patch</label>
                                </div>
                            </div>
                            <!-- col-3 -->
                            <div class="flex flex-col space-y-4 mt-4">
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.ac_service_checkbox" id="ac_service"
                                        @change="handleShow('ac_service')">
                                    <label class="text-[18px] pr-[7px]" for="ac_service">AC Service</label>&emsp;
                                    <select v-if="show.Ac" class="w-[16rem] h-[3rem] rounded-sm"
                                        style="border: 1px solid black;" v-model="requireService.ac" @change="shooo">
                                        <option value="" selected disabled hidden>Please select...</option>
                                        <option value="good">Good</option>
                                        <option value="better">Better</option>
                                        <option value="not_good">Not Good</option>
                                    </select>
                                </div>
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.battery_service_checkbox" id="battery"
                                        @change="handleShow('battery')">
                                    <label class="text-[18px] pr-1" for="battery">Battery</label>&emsp;&emsp;&emsp;
                                    <select v-if="show.battery" class="w-[16rem] h-[3rem] rounded-sm"
                                        style="border: 1px solid black;" v-model="requireService.battery"
                                        @change="shooo">
                                        <option value="" selected disabled hidden>Please select...</option>
                                        <option value="good">Good</option>
                                        <option value="better">Better</option>
                                        <option value="not_good">Not Good</option>
                                    </select>
                                </div>
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.wiper_service_checkbox" id="wiper" @change="handleShow('wiper')">
                                    <label class="text-[18px] pr-[1px]"
                                        for="wiper">Wiper</label>&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;
                                    <select v-if="show.wiper" class="w-[16rem] h-[3rem] rounded-sm"
                                        style="border: 1px solid black;" v-model="requireService.wiper" @change="shooo">
                                        <option value="" selected disabled hidden>Please select...</option>
                                        <option value="good">Good</option>
                                        <option value="better">Better</option>
                                        <option value="not_good">Not Good</option>
                                    </select>
                                </div>
                                <div class="flex flex-row items-center space-x-3">
                                    <input class="w-5 h-5 rounded-sm border border-black bg-gray-200" type="checkbox"
                                        v-model="show.car_wash_service_checkbox" id="car_wash"
                                        @change="handleShow('car_wash')">
                                    <label class="text-[18px] pr-[2px]" for="car_wash">Car Wash</label>&emsp;&emsp;
                                    <select v-if="show.car_wash" class="w-[16rem] h-[3rem] rounded-sm"
                                        style="border: 1px solid black;" v-model="requireService.car_wash"
                                        @change="shooo">
                                        <option value="" selected disabled hidden>Please select...</option>
                                        <option value="good">Good</option>
                                        <option value="better">Better</option>
                                        <option value="not_good">Not Good</option>
                                    </select>
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
                                        <label class="text-[16px]" for="LA">Last Alignment (kms)</label>
                                        <input class="w-[16rem]] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="LA" v-model="requireService.alignment.lastAlignment">
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[16px]" for="NA">Next Alignment (kms)</label>
                                        <input class="w-[16rem]] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="NA" v-model="requireService.alignment.nextAlignment"
                                            @change="shooo">
                                    </div>
                                </div>
                            </div>
                            <div v-if="show.rotation"
                                class="p-6 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg">
                                <h1 class="text-[20px] font-bold ml-1 mb-6">Tyre Rotation Details</h1>
                                <div class="flex flex-row space-x-[12rem] ml-[55px]">
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[16px]" for="rim">Rim</label>
                                        <input class="w-[16rem]] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="rim" v-model="requireService.rotation.rim">
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[16px]" for="wheel">Wheel</label>
                                        <input class="w-[16rem]] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="wheel" v-model='requireService.rotation.wheel'
                                            @change="shooo">
                                    </div>
                                </div>
                            </div>
                            <div v-if="show.oil_change"
                                class="p-6 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg">
                                <h1 class="text-[20px] font-bold ml-1 mb-6">Oil Service</h1>
                                <div class="flex flex-row space-x-[12rem] ml-[55px]">
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[16px]" for="oil_quality">Oil Quality</label>
                                        <div>
                                            <select class="w-[15rem] h-[3rem] rounded-sm"
                                                style="border: 1px solid black;" id="oil_quality"
                                                v-model="requireService.oil_change.oil_quality">
                                                <option value="" selected disabled hidden>Please select...</option>
                                                <option value="Good">Good</option>
                                                <option value="Ok">Ok</option>
                                                <option value="Change">Change</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[16px]" for="oil_quantity">Oil Quantity</label>
                                        <div>
                                            <select class="w-[15rem] h-[3rem] rounded-sm"
                                                style="border: 1px solid black;" id="oil_quantity"
                                                v-model="requireService.oil_change.oil_quantity" @change="shooo">
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
                                <h1 class="text-[20px] font-bold ml-1 mb-6">Balancing Details</h1>
                                <div class="flex flex-row justify-around">
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[1rem]" for="FL">Front-Left (gm)</label>
                                        <input class="w-[12rem] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="FL" v-model="requireService.balancing.fl">
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[1rem]" for="FR">Front-Right (gm)</label>
                                        <input class="w-[12rem] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="FR" v-model="requireService.balancing.fr">
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[1rem]" for="BL">Back-Left (gm)</label>
                                        <input class="w-[12rem] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="BL" v-model="requireService.balancing.bl">
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[1rem]" for="BR">Back-Right (gm)</label>
                                        <input class="w-[12rem] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="BR" v-model="requireService.balancing.br">
                                    </div>
                                    <div class="flex flex-col space-y-1">
                                        <label class="text-[1rem]" for="ST">Spare Tyre (gm)</label>
                                        <input class="w-[12rem] h-[3rem] rounded-sm border-solid border border-black"
                                            type="text" id="ST" v-model='requireService.balancing.st' @change="shooo">
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
                                            <label class="text-[16px]" for="FTS">Front Tyres (psi)</label>
                                            <input
                                                class="w-[12rem]] h-[3rem] rounded-sm border-solid border border-black"
                                                type="text" id="FTS" v-model="requireService.inflation.ft">
                                        </div>
                                        <div class="flex flex-col space-y-1">
                                            <label class="text-[16px]" for="RTS">Rear Tyres (psi)</label>
                                            <input
                                                class="w-[12rem]] h-[3rem] rounded-sm border-solid border border-black"
                                                type="text" id="RTS" v-model="requireService.inflation.rt"
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
                                    <option value="" selected>Please select...</option>
                                    <option value="Front Left">Front Left</option>
                                    <option value="Front Right">Front Right</option>
                                    <option value="Rear Left">Rear Left</option>
                                    <option value="Rear Right">Rear Right</option>
                                    <option value="Spare Tyre">Spare Tyre</option>
                                </select>
                                <div class="mt-[20px]">
                                    <label :for="'loadIndex' + index">Load Index<span v-if="tyre.mandatory && !tyre.loadIndex.trim()"
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
                                    <label :for="'speedRating' + index">Speed Rating<span v-if="tyre.mandatory && !tyre.speedRating.trim()"
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
                                    <label :for="'pattern' + index">Pattern<span v-if="tyre.mandatory && !tyre.pattern.trim()"
                                        class="text-red-500 font-bold">*</span></label>
                                    <select class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                        v-model="tyre.pattern"
                                        @change="getItemCode(tyre.brand, tyre.size, tyre.ttTl, tyre.pattern, index)">
                                        <option v-for="(pattern, index) in patterns[index]" :key="index">{{ pattern }}
                                        </option>
                                    </select>
                                </div>
                            </div>
                            <div class="ml-[300px]">
                                <div>
                                    <label :for="'ttTl' + index">TT/TL<span v-if="tyre.mandatory && !tyre.ttTl.trim()"
                                        class="text-red-500 font-bold">*</span></label>
                                    <select class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                        v-model="tyre.ttTl"
                                        @change="getPattern(tyre.brand, tyre.size, tyre.ttTl, index)">
                                        <option v-for="(type, index) in types[index]" :key="index">{{ type }}</option>
                                    </select>
                                </div>
                                <!-- <div class="mt-[20px]">
                                    <label :for="'item' + index">Item</label>
                                    <input class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                        :id="'item' + index" type="text" v-model="tyre.item" @change="saveData(index)">
                                </div> -->
                            </div>
                            <div class="ml-[400px]">
                                <FeatherIcon name="x" class="mt-0 ml-2 w-6 h-6 cursor-pointer text-red-500"
                                    @click="deleteTyreReplacement(index)" />
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
            <div v-if="currentstep == 4">
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
                <div class="pt-24 p-12">
                    <h1 class="text-[20px] font-bold mb-1">Items</h1>
                    <hr class="mt-2" :style="{ borderWidth: '2px', borderColor: 'gray' }">
                    <div class="pt-5">
                        <table
                            class="table-auto border border-collapse border-gray-800 w-auto shadow-md transition-shadow">
                            <thead>
                                <tr>
                                    <th class="border border-gray-800 px-4 py-4 w-[10rem]">SI.No</th>
                                    <th class="border border-gray-800 px-4 py-4 w-[10rem]">Item</th>
                                    <th class="border border-gray-800 px-4 py-4 w-[16rem]">Warehouse</th>
                                    <th class="border border-gray-800 px-4 py-4 w-[16rem]">Quantity</th>
                                    <th class="border border-gray-800 px-4 py-4 w-[10rem]">Rate</th>
                                    <th class="border border-gray-800 px-4 py-4 w-[10rem]">Amount</th>
                                </tr>
                            </thead>
                            <tbody class="border border-gray-800 text-center">
                                <tr v-for="(data, index) in tableData" :key="index">
                                    <td class="border border-gray-800 px-4 py-2 w-[10rem]">{{ index + 1 }}</td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <input type="text" v-model="data[billIndex].itemCode"
                                            class="w-[10rem] rounded-sm border-solid border border-black">
                                    </td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <div style="max-height: 200px; overflow-y: auto;">
                                            <select v-model="data[billIndex].sourceWarehouse"
                                                class="w-[10rem] rounded-sm border-solid border border-black">
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
                                        <input type="number" v-model="data[billIndex].requiredQuantity"
                                            @input="calculateTotals"
                                            class="w-[10rem] rounded-sm border-solid border border-black">
                                    </td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <input type="float" v-model="data[billIndex].rate" @input="calculateTotals"
                                            readonly
                                            class="w-[10rem] h-[2.6rem] pl-[0.7rem] rounded-sm border-solid border border-black text-justify">
                                    </td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <input type="text" v-model="data[billIndex].cost" readonly
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
                        <div class="mb-9">
                            <button class="bg-blue-500 text-white font-bold text-base p-3 rounded-lg mt-3"
                                @click="addNewRow(billIndex)">Add row</button>
                        </div>
                        <div class="flex">
                            <label>Discount Rate: <input type="text" v-model="discountRate"
                                    @input="calculateDiscountRate"
                                    class="w-[338px] h-[52px] rounded-sm border-solid border border-black"></label>
                            <label class="ml-auto pr-5">Total Amount:
                                <input type="text" :value="finalAmount.toFixed(2)" readonly
                                    class="w-[338px] h-[52px] rounded-sm border-solid border border-black cursor-not-allowed">
                            </label>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="Auth">
                <div class="flex justify-center space-x-5 p-5 mt-5 ml-3">
                    <button v-if="currentstep != 0"
                        class="bg-blue-500 w-[45%] text-white font-bold  text-base p-4 rounded-lg"
                        @click="previousPage">Previous
                    </button>
                    <button v-if="currentstep != 4 && initialNext"
                        class="bg-blue-500 w-[45%] text-white font-bold  text-base p-4 rounded-lg"
                        @click="nextPageAndHighlight">Next
                    </button>
                    <button v-if="currentstep == 4" @click="dataFinalSubmission"
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
import { ref, reactive, watch, computed, onMounted } from 'vue';
import { FeatherIcon } from 'frappe-ui'
import axios from 'axios';

const even = window.location.origin
const selectImg = ref(true);
const Auth = ref(true)
const incorrect = ref(false);
const currentstep = ref(0);

const data = reactive({
    selectedImgSrc: '',
    selectedAlt: ''
});

const headers = {
    'Content-Type': 'application/json',

    'Authorization': 'token 7fa0cf7915ad42d :2a784f5c29d213b'

}

const pin1 = ref('');
const pin2 = ref('');
const pin3 = ref('');
const pin4 = ref('');

const items = ref([])
const tableDetails = ref(false);
const addItem = () => {
    tableDetails.value = true;
    console.log(selectedBrand.value)
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
    console.log(data.selectedImgSrc, data.selectedAlt);
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
            console.log(Warehouse.value)
        })
})

onMounted(() => {
    axios.get(`${BaseURL}/api/method/tyre.api.get_vehicleBrand`, { headers: headers })
        .then(response => {
            vBrand.value = response.data.message
            console.log(vBrand.value)
        })
})


const get_Vmodel = (data) => {
    axios.post(`${BaseURL}/api/method/tyre.api.get_vehicleModel`, { model: data }, { headers: headers })
        .then(response => {
            console.log(response.data.message)
            vModel.value = response.data.message
            console.log(vModel.value)
        })
}

const getSize = (data, index) => {
    axios.post(`${BaseURL}/api/method/tyre.api.get_size`, { brand: data }, { headers: headers })
        .then(response => {
            console.log(index)
            if (index != -1) {
                console.log(sizes.value)
                sizes.value[index] = response.data.message;
            } else {
                rs.value = response.data.message;
            }
        })
}

const getOther = (brand, data, index) => {
    console.log(data)
    let i = 0;
    for (const co in sizes.value[index]) {
        const sizeData = sizes.value[index][i]
        if (sizeData.size == data) {
            tyres.value[index].loadIndex = sizeData.load_index;
            tyres.value[index].speedRating = sizeData.speed_rating;
            getType(brand, data, index)
        }
        i++;
    }
}
const getType = (brand, data, index) => {
    console.log(brand)
    console.log(size)
    console.log(index)
    axios.post(`${BaseURL}/api/method/tyre.api.get_type`, { brand: brand, size: data }, { headers: headers })
        .then(response => {
            console.log(response.data.message);
            types.value[index] = response.data.message;
            console.log(types.value)
        });
}
const getPattern = (brand, size, type, index) => {
    console.log(brand)
    console.log(size)
    console.log(index)
    console.log(type)
    axios.post(`${BaseURL}/api/method/tyre.api.get_pattern`, { brand: brand, size: size, tyer_type: type }, { headers: headers })
        .then(response => {
            console.log(response.data.message);
            patterns.value[index] = response.data.message;
        });
}
const getItemCode = (brand, size, type, pattern, index) => {
    console.log(brand)
    console.log(size)
    console.log(index)
    console.log(type)
    console.log(pattern)
    axios.post(`${BaseURL}/api/method/tyre.api.get_ItemCode`, { brand: brand, size: size, tyer_type: type, pattern: pattern }, { headers: headers })
        .then(response => {
            console.log(response.data.message[0]);
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
    console.log('space checking', plate);
    const spaced_plate = plate.match(/[a-zA-Z]{1,2}|\d+/g).join(" ");
    console.log('after spacing :', spaced_plate);
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
    console.log("data assignment", responseData.value);
    return responseData.value;
}
const check = ref(false)
const wrongSearchValue = ref(false);
const enable = ref(false)

const search = async () => {
    const data = {
        "license_plate": searchQuery.value
    };
    console.log('checking data', data);
    try {
        console.log("#$%^&")
        if (data.license_plate.trim() !== "") {
            console.log("*****")
            const response = await axios.post(`${BaseURL}/api/method/tyre.api.get_details`, { license_plate: data.license_plate }, { headers: headers });
            console.log(response.data.message);
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
                searchQuery.value = ''
            }

            else {
                check.value = true;
                enable.value = true;
                hasResponse.value = false;
                initial.value = false;
                afterResponse.value = true;
                initialNext.value = true
                searchQuery.value = ''
                console.log("Response:", response.data);
                return dataAssignment(response)
            }
        } else {
            showAlerts.value = true;
            searchValue.value = true;
            console.log("Please enter search value");
        }
    } catch (error) {
        console.error("Error:", error);
    }
};

const searchJobCard = ref('')
const hide = ref('false');
const jobCardDetails = reactive(ref([]));
const getJobCard = async () => {
    hide.value = true;
    try {
        const response = await axios.post(`${BaseURL}/api/method/tyre.api.get_jobcard_details`, { searchJobCard: searchJobCard.value }, { headers: headers });
        jobCardDetails.value = response.data.message;
        console.log(jobCardDetails.value);
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
    try {
        const response = await axios.get(`${BaseURL}/api/method/tyre.api.get_enquiry_details`, {
            params: {
                data: searchEnquiry.value
            },
            headers: headers
        });
        enquiryDetails.value = response.data.message;
        console.log(response.data.message);
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
        console.log(jobCardData.value);
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
// const currentstep = ref(0);
const maxStep = 4;

function previousPage() {
    if (currentstep.value > 0) {
        currentstep.value--;
        currentPage.value = getPageName(currentstep.value);
        console.log(currentPage.value)
    }
}

const showWarning = ref(false)
const close = () => {
    if (showWarning.value) {
        showWarning.value = false;
        showNewCustomer.value = true;
    }
    showAlerts.value = false;
    modifyAlert.value = false;
    successData.value = false;
    searchValue.value = false;
}
const closed = () => {
    showAlerts.value = false;
    if (vehicleNumber.value || vehicleExist.value) {
        vehicleNumber.value = false;
        vehicleExist.value = false;
        showNewVehicle.value = true
        console.log('vehicle page');
    }
    else if (notVehicleAlert.value || notCustomerAlert.value || notEmployeeAlert.value || notEmpDetailAlert.value || noVehicleNumber.value) {
        notVehicleAlert.value = false;
        notCustomerAlert.value = false;
        notEmployeeAlert.value = false;
        notEmpDetailAlert.value = false;
        noVehicleNumber.value = false;
        showNewCustomer.value = true;
        console.log('customer page');
    }
}

function nextPageAndHighlight() {
    if (currentstep.value < maxStep) {
        currentstep.value++;
        currentPage.value = getPageName(currentstep.value);
        console.log(responseData.value.message[0].name + "******")
        // if (currentstep.value == 3) {
        //     checkup(requireService)
        // }

        switch (currentstep.value) {
            case 1:
                jobCard["user"] = responseData.value.message[0].name;
                console.log(jobCard)
                console.log("****1****")
                break;
            case 2:
                jobCard["checkup"] = tyreDatas.value;
                for (let i = 0; i < tyreDatas.value.length; i++) {
                    const tyre = tyreDatas.value[i];
                    console.log('tyre name', tyre.tyre);
                    if (tyre.tyre) {
                        console.log('hi')
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
                console.log(jobCard)
                console.log("****2****")
                break;
            case 3:
                jobCard["service"] = requireService.value
                console.log(jobCard)
                console.log("****3****")
                addValue(requireService.value)
                break;
            case 4:
                jobCard["replace"] = tyres.value
                for (let i = 0; i < tyres.value.length; i++) {
                    const tyre = tyres.value[i];
                    console.log('tyre name', tyre.type);
                    if (tyre.type) {
                        console.log('hi')
                        if (tyre.loadIndex == '' || tyre.brand == '' || tyre.speedRating == '' || tyre.size == '' || tyre.pattern == '' || tyre.ttTl == '') {
                            tyre.mandatory = true;
                            currentstep.value = 3;
                            return;
                        }
                    }
                    else {
                        tyre.mandatory = false
                    }
                }
                console.log(jobCard)
                console.log("****4****")
                addValue(tyres.value, replace)
                break;
            case 5:
                checkup(jobCard);
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
    if (initialNext.value) {
        currentPage.value = page;
        currentstep.value = step;
    }
};
const vehicleDetails = ref({
    name: '',
    vehicle_brand: '',
    vehicle_model: '',
    chassis_no: '',
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
    chassis_no: '',
    fuel_type: '',
    last_odometer_reading: '',
    tyre_change: '',
    alignment: ''
});

const showConfirmation = ref(false);
const newVehicleSave = ref(false);
const newCustomerSave = ref(false);
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

    fieldNames.forEach(fieldName => {
        const value = vehicleData.value[fieldName];
        if (value == '') {
            return;
        }
        data[fieldName] = value;
    });

    const searchData = data.name;
    console.log("searchData", searchData);
    if (!searchData) {
        showNewVehicle.value = false
        showAlerts.value = true
        vehicleNumber.value = true
        return;
    }

    console.log('vehicle number:', data.name);
    const isVehicleExist = await returnSearch(searchData);
    const checkingVehicleExist = isVehicleExist && isVehicleExist.message && isVehicleExist.message.length > 0 ? isVehicleExist.message == "Enter a Valid vehicle number" ? 'no data' : isVehicleExist.message[0].name : 'empty'
    console.log('is vehicle exist:', checkingVehicleExist);
    if (checkingVehicleExist && checkingVehicleExist !== 'empty') {
        showNewVehicle.value = false
        showAlerts.value = true
        vehicleExist.value = true
        return;
    }
    else if (isVehicleExist && isVehicleExist == 'Enter a Valid vehicle number') {
        showAlerts.value = true;
        noValidVehicleNumber.value = true;
    }
    else {
        showConfirmation.value = true;
        newVehicleSave.value = true;
        showNewVehicle.value = false;
    }
};

const confirmSave = async () => {
    console.log('confirm page');
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
    console.log('searchdata in confirm page:', searchData);
    try {
        const response = await axios.post(`${BaseURL}/api/method/tyre.api.store_vehicle_details`, { data: JSON.stringify(data) }, { headers: headers });
        console.log('vehicle add after response', response);
        if (responseData.value && responseData.value.message) {
            enable.value = true;
            check.value = true;
            hasResponse.value = false;
            showAlerts.value = true
            successData.value = true;
            dataAssignment(response);
            console.log("vehicle data in responseData.value:", responseData.value.message[0].alignment);
            console.log("vehicle data in responseData.value:", responseData.value.message[0].name);
            console.log("vehicle data in responseData.value:", responseData.value.message[0]);
            console.log("vehicle data in responseData.value:", responseData.value);
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
        chassis_no: responseData.value.message[0].chassis_no,
        fuel_type: responseData.value.message[0].fuel_type,
        last_odometer_reading: responseData.value.message[0].last_odometer_reading,
        tyre_change: responseData.value.message[0].tyre_change,
        alignment: responseData.value.message[0].alignment
    };
    console.log(modifiedData)
    try {
        const response = await axios.post(`${BaseURL}/api/method/tyre.api.store_vehicle_details`, { data: JSON.stringify(modifiedData) }, { headers: headers });
        console.log(response);
        returnSearch(name)
        showModifyVehicle.value = false;
        showAlerts.value = true;
        modifyAlert.value = true;
    } catch (error) {
        console.error(error);
    }
};

const updateEmployeeType = (employee) => {
    console.log(employee);
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
const setPrimary = () => {
    let firstDriverIndex = -1;
    let firstContactPersonIndex = -1;

    // Find the index of the first driver and contact person
    customerData.value.employees.forEach((employee, index) => {
        if (employee.type === 'current_driver' && firstDriverIndex === -1) {
            firstDriverIndex = index;
        } else if (employee.type === 'contact_person' && firstContactPersonIndex === -1) {
            firstContactPersonIndex = index;
        }
    });

    // Check the checkbox for the first driver and contact person
    if (firstDriverIndex !== -1) {
        customerData.value.employees[firstDriverIndex].primary = true;
        console.log(`Primary checkbox set for the first driver at index ${firstDriverIndex}`);
    } else {
        console.log(`No driver found.`);
    }

    if (firstContactPersonIndex !== -1) {
        customerData.value.employees[firstContactPersonIndex].primary = true;
        console.log(`Primary checkbox set for the first contact person at index ${firstContactPersonIndex}`);
    } else {
        console.log(`No contact person found.`);
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
            console.log("cbdsicbewcbdcnwdocn:", newEmployee.whatsapp);
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
            console.log(newEmployee.custom_whatsapp)
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

const customerData = ref({
    name: '',
    current_owner: '',
    owner_mobile_no: '',
    employees: employees.value,
    whatsappChecked: 0,
    callChecked: 0,
    smsChecked: 0,
});

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

const addCustomerData = async () => {
    const name = responseData.value.message[0].name.trim();
    console.log(name)
    const existingData = await returnSearch(name);
    console.log('filtering process', existingData.message[1].current_owner);
    console.log('vehicle number during customer add:', existingData.message[0].name);
    if (!existingData.message[0].name) {
        console.log("Vehicle not exist!");
        showAlerts.value = true;
        notVehicleAlert.value = true;
        showNewCustomer.value = false
        return
    }
    else if (existingData.message[0].name && !existingData.message[1].current_owner) {
        const ownerName = customerData.value.current_owner.trim();
        const ownerMobile = customerData.value.owner_mobile_no.trim();

        if (!ownerName && !ownerMobile && !name) {
            showAlerts.value = true;
            notCustomerAlert.value = true
            showNewCustomer.value = false
            return;
        }
        if (employees.value.length === 0) {
            showAlerts.value = true
            notEmployeeAlert.value = true
            showNewCustomer.value = false
            return;
        }
        const isAnyEmployeeDataMissing = employees.value.some(employee => {
            return !employee.driver_name.trim() || !employee.mobile_no.trim();
        });
        if (isAnyEmployeeDataMissing) {
            showAlerts.value = true;
            notEmpDetailAlert.value = true;
            showNewCustomer.value = false
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
        console.log('before checking customer data', data);
        try {
            const response = await axios.post(`${BaseURL}/api/method/tyre.api.store_customer_details`, { data: JSON.stringify(data) }, { headers: headers })
            check.value = true;
            console.log(response);
            if (response) {
                showNewCustomer.value = false;
                dataAssignment(response)
                showAlerts.value = true;
                successData.value = true;
                removeCustomerData()
                console.log("Customer data in responseData.value:", responseData.value.message[1].owner_mobile_no);
                console.log("Customer data in responseData.value:", responseData.value.message[1].current_owner);
                console.log(responseData.value.message[1].call);
                console.log("Customer data in responseData.value:", responseData.value.message[1]);
                console.log("Customer data in responseData.value.message:", responseData.value.message);
                if (name) {
                    returnSearch(name)
                }
            } else {
                console.log("responseData.value or responseData.value.message is undefined");
            }
            console.log("Owner name:", data.current_owner);
            console.log("Owner mobile:", data.owner_mobile_no);

            data.employees.forEach(employee => {
                console.log("Employee Name:", employee.driver_name);
                console.log("Employee Type:", employee.type);
                console.log("Employee Type:", employee.mobile_no);
            });

            console.log(data);
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
    console.log('modified data', name);
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
        console.log('index driver', i);
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
        console.log('index contact', i);
    });

    console.log('modify checking', modifiedData);
    try {
        const response = await axios.post(`${BaseURL}/api/method/tyre.api.store_customer_details`, { data: JSON.stringify(modifiedData) }, { headers: headers });
        check.value = true;
        console.log(response);
        returnSearch(name)
        showModifyCustomer.value = false;
        showAlerts.value = true;
        modifyAlert.value = true;
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
    alignment: 0,
    oil_change: 0,
    inflation: 0,
    tyre_edge: 0,
    mushroom_patch: 0,
    battery: 0,
    car_wash: 0,
    rotation: 0,
    balancing: 0,
    puncture: 0,
    tyre_patch: 0,
    ac_service: 0,
    wiper: 0
})

const handleCustomer = async () => {
    if (!searchMobile.value) {
        showNewCustomer.value = false;
        if (customerData.value.current_owner && customerData.value.owner_mobile_no) {
            showConfirmation.value = true;
            newCustomerSave.value = true;
        }
        else {
            showWarning.value = true;
            setTimeout(() => {
                showWarning.value = false;
                showNewCustomer.value = true;
            }, 1000);
        }
    }
    else {
        showNewCustomer.value = false
        showAlerts.value = true;
        cannotSave.value = true;
        setTimeout(() => {
            showAlerts.value = false;
            cannotSave.value = false;
            showNewCustomer.value = true
        }, 1000);
    }
}

const popItems = ref([]);
const billPopup = ref('false');
const confirmCustomerSave = async () => {
    showConfirmation.value = false;
    newCustomerSave.value = false;
    if (boolDetails.state == 1) {
        alert("Unable to edit")
        return
    }
    const customerDetails = {
        current_owner: customerData.value.current_owner,
        owner_mobile_no: customerData.value.owner_mobile_no,
        whatsapp: customerData.value.whatsappChecked,
        call: customerData.value.callChecked,
        sms: customerData.value.smsChecked,
        items: items.value,
        services: serviceDetails.value
    }
    try {
        const response = await axios.post(`${BaseURL}/api/method/tyre.api.lead`, customerDetails, { headers: headers })
        showAlerts.value = true;
        successData.value = true;
        console.log('response from customer details', response.data);
        popItems.value = response.data.message;

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
        billPopup.value = 'true';

    } catch (error) {
        console.log("Temporary customer details page:", error)
    }
}

const searchMobile = ref('')
const boolDetails = reactive({
    state: 0,
});

const handleSearch = async () => {
    if (searchMobile.value) {
        const response = await axios.get(`${BaseURL}/api/method/tyre.api.lead_details`, {
            params: {
                data: searchMobile.value
            },
            headers: headers
        });
        leadDetails.value = response.data.message;
        boolDetails.state = 1;

        console.log('lead details', leadDetails.value);
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


const selectedBrandVariants = computed(() => {
    console.log('checking', selectedBrand.value);
    if (selectedBrand.value) {
        for (let brand of responseData.value.message) {
            if (brand.name === selectedBrand.value) {
                console.log('variants checking', brand.variants);
                return brand.variants
            }
        }
    }
});
const afterResponse = ref(false);
const handleEnquiry = async () => {
    if(!handle.value){
        hasResponse.value = true;
        try {
            const response = await axios.get(`${BaseURL}/api/method/tyre.api.stock_details`);
            console.log('response data for customer details', response.data);
            responseTyreData.value = response.data;
            console.log(responseTyreData.value);
            for (let tyre of responseTyreData.value.message) {
                console.log(tyre.name);
            }
        } catch (error) {
            console.log('Error fetching tyre data:', error);
        }
    }
    else{
        handle.value = false
        hasResponse.value = false;
        console.log("Else block")
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
    console.log('checking data', data.license_plate);
    try {
        if (data.license_plate.trim() !== "") {
            console.log("**&**")
            const response = await axios.post(`${BaseURL}/api/method/tyre.api.get_details`, { license_plate: JSON.stringify(data.license_plate) }, { headers: headers });
            check.value = true;
            console.log('returnSearch data', response);
            if (response.data.message === "") {
                // responseData.value = {
                //     message: [{
                //         name: '',
                //         vehicle_brand: '',
                //         vehicle_model: '',
                //         chassis_no: '',
                //         fuel_type: '',
                //         last_odometer_reading: '',
                //         tyre_change: '',
                //         alignment: ''
                //     },
                //     {
                //         current_owner: '',
                //         owner_mobile_no: '',
                //         call: '',
                //         whatsapp: '',
                //         sms: '',
                //         current_driver: [{
                //             current_driver: '',
                //             name: '',
                //             mobile_no: '',
                //             call: '',
                //             whatsapp: '',
                //             sms: ''

                //         }],
                //         contact_person: [{
                //             contact_person_name: '',
                //             contact_person_mobile: '',
                //             custom_call: '',
                //             custom_whatsapp: '',
                //             custom_sms: ''
                //         }]
                //     },
                //     {
                //         current_driver: [{
                //             current_driver: '',
                //             name: '',
                //             mobile_no: '',
                //             call: '',
                //             whatsapp: '',
                //             sms: ''

                //         }],
                //         contact_person: [{
                //             contact_person_name: '',
                //             contact_person_mobile: '',
                //             custom_call: '',
                //             custom_whatsapp: '',
                //             custom_sms: ''
                //         }]
                //     }
                //     ]
                // };
                
                console.log(response.data);
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
                } else if (showNewCustomer.value) {
                    showNewCustomer.value = false;
                    showAlerts.value = true;
                    noCustomerValidVehicleNumber.value = true;
                }
                return response.data.message;
            }
            else {
                console.log('cutomer details checking now', responseData.value);
                initial.value = false
                initialNext.value = true
                return dataAssignment(response)
            }
        } else {
            showNewCustomer.value = false;
            showAlerts.value = true;
            noVehicleNumber.value = true;
            console.log("Enter Vehicle Number");
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
    console.log(data);
    if (data) {
        axios.post(`${BaseURL}/api/method/tyre.api.delete_modified_customers`, { data: data }, { headers: headers });
        responseData.value.message[1].current_driver.splice(index, 1);
    } else {
        console.log(error);
    }
    // catch(error){
    // }
};
const removeEmployee3 = (index) => {
    const data = {
        "contact_person_name": responseData.value.message[1].contact_person[index].contact_person_name,
        "parentfield": responseData.value.message[1].contact_person[index].parentfield,
        "contact_person_mobile": responseData.value.message[1].contact_person[index].contact_person_mobile,
        "name": responseData.value.message[1].contact_person[index].parent
    }
    console.log(data);
    if (data) {
        axios.post(`${BaseURL}/api/method/tyre.api.delete_modified_customers`, { data: data }, { headers: headers });
        responseData.value.message[1].contact_person.splice(index, 1);
    } else {
        console.log(error);
    }
};
const removeEmployee1 = (index) => {
    if (sample22.value != 0) {
        employees.value.splice(index, 1);
        setPrimary();
    }
};

const deleteVehicle = () => {
    showDeleteConfirmation.value = true;
}
const deleteConfirmation = ref(false);
const confirmDelete = async (vehicle) => {
    const data = {
        name: vehicle
    };
    console.log("Vehicle delete", data)
    showDeleteConfirmation.value = false;
    try {
        const response = await axios.post(`${BaseURL}/api/method/tyre.api.delete_vehicle`, { data: JSON.stringify(data) }, { headers: headers })
        console.log("delete response", response)
        if (response.data.message == "deleted") {
            showAlerts.value = true;
            deleteConfirmation.value = true;
            setTimeout(() => {
                showAlerts.value = false;
                deleteConfirmation.value = false;
            }, 2000);
            // alert("vehicle deleted successfully!")
            returnSearch(vehicle)
        }
    } catch (error) {
        console.log("Vehicle delete error:", error)
    }
}
const cancelDelete = () => {
    showDeleteConfirmation.value = false;
    console.log("hi cancel")
}


//==========================================================>>> 5 point checkup <<<==========================================================================//

const tyreDatas = ref([{ tyre: '', depth: '', pressure: '', comment: '', wear: false, cut: false, mark: false, damage: false, bulge: false, puncture: false }]);

const sampleValue = reactive({
    index: ref(1),
})

const addTyre = () => {
    if (sampleValue.index < 5) {
        tyreDatas.value.push({ tyre: '', depth: '', pressure: '', comment: '', wear: false, cut: false, mark: false, damage: false, bulge: false, puncture: false });
        sampleValue.index++;
    }
    //   tyreDatas.value.push({ tyre: '', depth: '', pressure: '', comment: '', wear: false, cut: false, mark: false, damage: false, bulge: false, puncture: false });
};


const updateTyreData = (index) => {
    const tyre = tyreDatas.value[index];
    // console.log('Updated tyre data:', tyre);
    // console.log(tyreDatas.value);
};

const deleteTyre = (index) => {
    if (sampleValue.index > 1) {
        tyreDatas.value.splice(index, 1);
        sampleValue.index--;
        console.log(tyreDatas.value);
    }
    //   tyreDatas.value.splice(index, 1);
    //   console.log(tyreDatas.value);
};
//========================================================>>> Required Services <<<============================================================================//

let selectedCheckbox = null;

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
    mushroom_path_checkbox: false,
})

function handleCheckboxChange(checkboxId) {
    if (this.selectedCheckbox === checkboxId) {
        selectedCheckbox = null;
    } else {
        selectedCheckbox = checkboxId;
        const otherCheckboxId = checkboxId === 'air' ? 'nitrogen' : 'air';
        requireService.value.inflation.type = selectedCheckbox;
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
            console.log(show.value.inflation_air);
            console.log(show.value.inflation_nitrogen);
        }
    }
}
const requireService = ref({
    Alignment: false,
    Rotation: false,
    Oil_change: false,
    Balancing: false,
    Inflation: false,
    AcService: false,
    Battery: false,
    Wiper: false,
    CarWash: false,
    alignment: {
        lastAlignment: '',
        nextAlignment: ''
    },
    rotation: {
        rim: '',
        wheel: ''
    },
    oil_change: {
        oil_quality: '',
        oil_quantity: ''
    },
    balancing: {
        fl: '',
        fr: '',
        bl: '',
        br: '',
        st: ''
    },
    inflation: {
        type: '',
        ft: '',
        rt: ''
    },
    ac: '',
    battery: '',
    wiper: '',
    car_wash: '',
    puncture: false,
    tyre_edge: false,
    tyre_patch: false,
    mashroom_patch: false,
})
function checkup(data) {
    console.log("******")
    console.log(data)
    try {
        const response = axios.post(`${BaseURL}/api/method/tyre.api.job_card`, { data: JSON.stringify(data) }, { headers: headers });
        console.log(response);
    } catch (error) {
        console.error("error");
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
                requireService.value.ac = '';
            }
            break;
        case 'battery':
            show.value.battery = !show.value.battery;
            requireService.value.Battery = show.value.battery;
            if (show.value.battery == false) {
                requireService.value.battery = '';
            }
            break;
        case 'wiper':
            show.value.wiper = !show.value.wiper;
            requireService.value.Wiper = show.value.wiper;
            if (show.value.wiper == false) {
                requireService.value.wiper = '';
            }
            break;
        case 'car_wash':
            show.value.car_wash = !show.value.car_wash;
            requireService.value.CarWash = show.value.car_wash;
            if (show.value.car_wash == false) {
                requireService.value.car_wash = '';
            }
            break;
        case 'alignment':
            show.value.alignment = !show.value.alignment;
            requireService.value.Alignment = show.value.alignment;
            if (show.value.alignment == false) {
                requireService.value.alignment.lastAlignment = '';
                requireService.value.alignment.nextAlignment = '';
            }
            break;
        case 'rotation':
            show.value.rotation = !show.value.rotation;
            requireService.value.Rotation = show.value.rotation;
            if (show.value.rotation == false) {
                requireService.value.rotation.rim = '';
                requireService.value.rotation.wheel = '';
            }
            break;
        case 'oil_change':
            show.value.oil_change = !show.value.oil_change;
            requireService.value.Oil_change = show.value.oil_change;
            if (show.value.oil_change == false) {
                requireService.value.oil_change.oil_quality = '';
                requireService.value.oil_change.oil_quantity = '';
            }
            break;
        case 'balancing':
            show.value.balancing = !show.value.balancing;
            requireService.value.Balancing = show.value.balancing;
            if (show.value.balancing == false) {
                requireService.value.balancing.fl = '';
                requireService.value.balancing.fr = '';
                requireService.value.balancing.bl = '';
                requireService.value.balancing.br = '';
                requireService.value.balancing.st = '';
            }
            break;
        case 'inflation':
            show.value.inflation = !show.value.inflation;
            requireService.value.Inflation = show.value.inflation;
            if (show.value.inflation == false) {
                requireService.value.inflation.type = '';
                requireService.value.inflation.ft = '';
                requireService.value.inflation.rt = '';
            }
            break;
    }
}

function handelCheck(data) {
    switch (data) {
        case 'puncture':
            show.puncture_checkbox = !show.puncture_checkbox;
            if (show.puncture_checkbox == true) {
                requireService.value.puncture = true;
            } else {
                requireService.value.puncture = false;
            }
            break
        case 'tyre_edge':
            show.tyre_edge_checkbox = !show.tyre_edge_checkbox;
            if (show.tyre_edge_checkbox == true) {
                requireService.value.tyre_edge = true;
            } else {
                requireService.value.tyre_edge = false;
            }
            break;
        case 'tyre_patch':
            show.tyre_path_checkbox = !show.tyre_path_checkbox;
            if (show.tyre_path_checkbox == true) {
                requireService.value.tyre_patch = true;
            } else {
                requireService.value.tyre_patch = false;
            }
            break;
        case 'mushroom_patch':
            show.mushroom_path_checkbox = !show.mushroom_path_checkbox;
            if (show.mushroom_path_checkbox == true) {
                requireService.value.mashroom_patch = true;
            } else {
                requireService.value.mashroom_patch = false;
            }
            break;
    }
}

//===================================================>>> Replacement Tyre Details <<<========================================================================//

const tyrePositions = ['Front Left', 'Front Right', 'Rear Left', 'Rear Right', 'Spare'];
const replace = reactive({
    target: false
});
let billIndex = 0;
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
    mandatory: false,
    status: false
}]);

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
    //   tyres.value.splice(index, 1)
}

let step = ref(0)
function addValue(data, replace) {
    // Check if data is an array
    console.log(data)
    if (Array.isArray(data)) {
        console.log(replace.target);
        // Data is a list (array)
        if (!replace.target) {
            data.forEach(item => {
                console.log(item);
                console.log(item.item);

                // Initialize existingItemIndex to -1
                let existingItemIndex = -1;

                // Check if tableData.value[billIndex] is an array
                if (Array.isArray(tableData.value)) {
                    console.log(tableData.value);
                    name: for (let index = 0; index < tableData.value.length; index++) {
                        const rowData = tableData.value[index];
                        console.log(rowData);
                        console.log("*****");
                        for (let i = 0; i < rowData.length; i++) {
                            const items = rowData[i];
                            console.log(items);
                            console.log(items.itemCode);
                            console.log(item.item);
                            if (items.itemCode === item.item) {
                                existingItemIndex = index;
                                console.log(existingItemIndex);
                                break name;
                            }
                        }
                    }
                    // Find the index of the item with the same itemCode, if it exists
                    // existingItemIndex = tableData.value[billIndex].findIndex(existingItem => existingItem.itemCode === item.item);
                }

                console.log(tableData.value);
                console.log(existingItemIndex);
                console.log(item.status)
                console.log(billIndex)

                if (existingItemIndex > -1 && !item.status) {
                    // Increase the quantity of the existing item
                    console.log(tableData.value[existingItemIndex][0].requiredQuantity);
                    tableData.value[existingItemIndex][0].requiredQuantity++;
                    console.log(tableData.value[existingItemIndex][0].requiredQuantity)
                    console.log(tableData.value[existingItemIndex][0].requiredQuantity);
                    // Remove the existing item from the array
                    tableData.value.splice(existingItemIndex, 1);
                } else {
                    // If tableData.value[billIndex] is not an array, initialize it
                    if (!Array.isArray(tableData.value[billIndex])) {
                        tableData.value[billIndex] = [];
                    }

                    // Create a new object for the item
                    console.log(item.item)
                    const newData = {
                        itemCode: item.item,
                        sourceWarehouse: '',
                        rate: item.rate,
                        requiredQuantity: 1, // Set initial quantity to 1
                        cost: ''
                    };

                    // Push the new object into the array at the specified billIndex
                    tableData.value[billIndex].push(newData);
                }

                // Mark the item as processed
                item.status = true;


                calculateTotals();
                billIndex++;
            });
        }
        replace.target = true;
    }



    else if (typeof data === 'object') {
        for (const key in data) {
            if (Object.hasOwnProperty.call(data, key)) {
                if (data[key] === true) {
                    let itemExists = false;
                    tableData.value.forEach((rowData, index) => {
                        rowData.forEach(item => {
                            if (item.itemCode === key) {
                                itemExists = true;
                            }
                        });
                    });
                    if (!itemExists) {
                        const newData = {
                            itemCode: key,
                            sourceWarehouse: '',
                            rate: '',
                            requiredQuantity: 1,
                            cost: ''
                        };
                        if (!Array.isArray(tableData.value[billIndex])) {
                            tableData.value[billIndex] = [];
                        }
                        tableData.value[billIndex].push(newData);
                        calculateTotals();

                        billIndex++;
                    }
                }
            }
        }
    }
    // Update the step variable
    step = billIndex;
}

//===================================================>>> Billing Details <<<=========================================================================================//

const tableData = ref([]);
const totalRate = ref(0);
const totalQuantity = ref(0);
const totalCost = ref(0);
const discountRate = ref();
const finalAmount = ref();

const calculateTotals = () => {
    let sumRate = 0;
    let sumQuantity = 0;
    let sumCost = 0;

    tableData.value.forEach(row => {
        // Assuming each row is an object
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

    // calculateDiscountRate();
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
    console.log("stepindex", step)
    if (!Array.isArray(tableData.value[step])) {
        tableData.value[step] = [];
    }

    // Push a new object into tableData[billIndex]
    tableData.value[step].push({
        itemCode: '',
        sourceWarehouse: '',
        rate: '',
        requiredQuantity: '',
        cost: '',
    });
    step++;
    billIndex = step
    console.log("billIndex", billIndex)
    console.log("^&*()_")
    // Calculate totals after adding the new row
    // calculateTotals();

    console.log('New row added at billIndex:', billIndex);
};


const submitData = () => {
    console.log("hi", tableData.itemCode, totalRate, totalQuantity, totalCost, discountRate, finalAmount);
}
const removeRow = (index) => {
    console.log(billIndex)
    console.log(step)
    tableData.value.splice(index, 1);
    console.log(tableData.value)
    step--;
    billIndex = step;
    console.log("billIndex:", billIndex)
    console.log("stepIndex:", step)
    calculateTotals();
};
const showConfirm = ref(false)
const dataFinalSubmission = () => {
    showConfirm.value = true;
    console.log("showConfirm", showConfirm.value);
}
const confirmDataSave = () => {
    showConfirm.value = false;
    console.log("Final submission process going on....");
    jobCard["bill"] = tableData.value
    console.log(jobCard)
    checkup(jobCard)
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
    /* Center align the items horizontally */
}
</style>
