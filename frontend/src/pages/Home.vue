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
                        <div>
                            <input type="button"
                                class="bg-blue-500 w-[150px] text-white font-bold text-base p-4 rounded-lg ml-3"
                                value="Create Customer">
                            <div class="flex justify-end">
                                <FeatherIcon name="arrow-right" class="w-8 h-8 cursor-pointer text-blue-500"
                                    @click="nextPageAndHighlight" />
                            </div>
                        </div>
                        <div class="flex justify-center m-5">
                            <input type="text" class="w-[338px] h-[52px] rounded-sm border-solid border border-black"
                                v-model="searchQuery" @keyup.enter="search" placeholder="Enter your Vehicle Number">
                            <button class="bg-blue-500 w-[150px] text-white font-bold text-base p-4 rounded-lg ml-3"
                                @click="search">Search</button>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <Card>
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
                                                <label>Odometer Value&nbsp;&nbsp;:&nbsp;</label>
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
                            <Card>
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
                                                    {{ responseData && responseData.message && responseData &&
                responseData.message && responseData.message[2][0]?.full_name || 'No data' }}
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
                        </div>
                        <!-- <div class=" h-64" v-if="check == false"></div> -->

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
                                    <p class="m-2">Vehicle Number <br>
                                        <input type="text"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.name" placeholder="Enter your Vehicle Number">
                                    </p>
                                    <p class="m-2">Vehicle Brand <br>
                                        <input type="text"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.vehicle_brand" placeholder="Enter Vehicle Brand">
                                    </p>
                                    <p class="m-2">Vehicle Model <br>
                                        <input type="text"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.vehicle_model" placeholder="Enter Vehicle Model">
                                    </p>
                                    <p class="m-2">Chassis No <br>
                                        <input type="text"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.chassis_no" placeholder="Enter Chassis No">
                                    </p>
                                    <p class="m-2">Fuel Type <br>
                                        <select v-model="vehicleData.fuel_type"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black">
                                            <option value="Petrol">Petrol</option>
                                            <option value="Diesel">Diesel</option>
                                            <option value="EV">Electical Vehicle</option>
                                        </select>
                                    </p>
                                    <p class="m-2">Odometer Value <br>
                                        <input type="text"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.last_odometer_reading"
                                            placeholder="Enter Odometer Value">
                                    </p>
                                    <p class="m-2">Tyre Change (kms) <br>
                                        <input type="text"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.tyre_change" placeholder="Enter Tyre Change">
                                    </p>
                                    <p class="m-2">Alignment (kms) <br>
                                        <input type="text"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="vehicleData.alignment" placeholder="Enter Alignment">
                                    </p>
                                    <div class="m-3 mt-4 flex flex-row space-x-[70px]">
                                        <button class="bg-green-500 w-[100px] text-white font-bold 0 p-2 rounded"
                                            @click="addVehicleData">Add</button>
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
                                    <p class="m-2">Odometer Value <br>
                                        <input type="text" v-if="check"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="responseData.message[0].last_odometer_reading"
                                            placeholder="Enter Odometer Value">
                                    </p>
                                    <p class="m-2">Tyre Change (kms) <br>
                                        <input type="text" v-if="check"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            v-model="responseData.message[0].tyre_change"
                                            placeholder="Enter Tyre Change">
                                    </p>
                                    <p class="m-2">Alignment (kms) <br>
                                        <input type="text" v-if="check"
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
                            <div class="max-w-md w-full bg-white shadow-xl h-full overflow-y-auto relative">
                                <button class="absolute to text-gray pt-5 font-bold p-2 right-2 px-2 py-1 rounded"
                                    @click="addCustomer">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M6 18L18 6M6 6l12 12" />
                                    </svg>
                                </button>
                                <div class="p-8 mt-[150px]">
                                    <div class="pb-4 m-2 grid grid-cols-2" v-if="handle">
                                        <input type="tel"
                                            class="w-[19rem] h-[3rem] mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter Your Mobile Number">
                                        <div class="w-[3rem] h-[3rem] mt-1 ml-[7.6rem] bg-blue-600 rounded-sm">
                                            <FeatherIcon name="search"
                                                class="m-2 w-8 h-8 cursor-pointer text-gray-100" />
                                        </div>
                                    </div>
                                    <div class="grid grid-cols-2">
                                        <div class="mt-0.5">
                                            <h2 class="text-2xl font-semibold mb-4">Customer Details</h2>
                                        </div>
                                        <span class="ml-[4rem]">
                                            <input type="checkbox" v-model="handle" @click="handleEnquiry"
                                                class="bg-gray-300 rounded-sm pb-4">&nbsp;&nbsp;<label>Enquiry</label>
                                        </span>
                                    </div>
                                    <hr class="dark-hr">
                                    <p class="m-2" v-if="!handle">Vehicle Number <br>
                                        <input type="text" v-model="customerData.name"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter your Vehicle Number">
                                    </p>
                                    <p class="m-2">Customer Name <br>
                                        <input type="text" v-model="customerData.current_owner"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter Customer Name">
                                    </p>
                                    <p class="m-2">Customer Mobile No <br>
                                        <input type="text" v-model="customerData.owner_mobile_no"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter Customer Mobile No.">
                                    </p>
                                    <input type="checkbox" v-model="customerData.whatsappChecked"
                                        class="bg-gray-300 rounded-sm">&nbsp;&nbsp; <label>WhatsApp</label>
                                    <span class="ml-5">
                                        <input type="checkbox" v-model="customerData.callChecked"
                                            class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>call</label>
                                    </span>
                                    <span class="ml-5">
                                        <input type="checkbox" v-model="customerData.smsChecked"
                                            class="bg-gray-300 rounded-sm">&nbsp;&nbsp;<label>SMS</label>
                                    </span>
                                    <div v-if="!handle">
                                        <div v-for="(employee, index) in employees" :key="index" class="mt-2">
                                            <hr class="dark-hr m-4">
                                            <p class="m-2">Employee Name
                                                <button
                                                    class="bg-blue-500 w-[100px] text-white font-bold  text-base p-4 rounded-lg mb-1 float-right"
                                                    @click="removeEmployee1(index)">Remove</button> <br>
                                                <br>
                                                <input type="text" v-model="employee.driver_name"
                                                    class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                                    placeholder="Enter your Name">
                                            </p>
                                            <p class="m-2">Employee Type<br>
                                                <select v-model="employee.type"
                                                    class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black">
                                                    <option value="current_driver">Driver</option>
                                                    <option value="contact_person">Contact Person</option>
                                                </select>
                                            </p>
                                            <p class="m-2">Phone <br>
                                                <input type="text" v-model="employee.mobile_no"
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
                                    <div v-else>
                                        <label>Tyre</label>
                                        <hr class="dark-hr">
                                        <div class="grid grid-cols-3 gap-4">
                                            <div class="flex flex-col ml-3">
                                                <label class="mt-2">Brand</label>
                                                <select class="w-[75%] h-[100%] rounded-sm border-solid border border-black" v-model="selectedBrand">
                                                    <option v-for="tyre in responseData.message" :key="tyre" >{{ tyre.name }} </option>
                                                </select>
                                            </div>
                                            <div class="flex flex-col ml-3">
                                                <label class="mt-2">Size</label>
                                                <!-- <select class="w-[75%] h-[100%] rounded-sm border-solid border border-black" v-model="selectedBrand">
                                                    <option v-for="(tyre,index) in responseData.message[0].variants" :key="index" >{{ index }} </option> -->
                                                <!-- </select> -->
                                              <!-- <input class="w-[75%] h-[100%] rounded-sm border-solid border border-black" type="text" v-model="size"> -->
                                            </div>
                                            <div class="flex flex-col ml-3">
                                              <label class="mt-2">Quantity</label>
                                              <input class="w-[75%] h-[100%] rounded-sm border-solid border border-black" type="text" v-model="quantity">
                                            </div>
                                          </div>
                                            <label>Services</label>
                                        <hr class="dark-hr">
                                        <div class="grid grid-cols-2 mt-5">
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.alignment" class="bg-gray-300 rounded-sm"> <label>Alignment</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.rotation" class="bg-gray-300 rounded-sm"> <label>Rotation</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.oil_change" class="bg-gray-300 rounded-sm"> <label>Oil Change</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.balancing" class="bg-gray-300 rounded-sm"> <label>Balancing</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.inflation" class="bg-gray-300 rounded-sm"> <label>Inflation</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.puncture" class="bg-gray-300 rounded-sm"> <label>Puncture</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.tyre_edge" class="bg-gray-300 rounded-sm"> <label>Tyre Edge</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.tyre_patch" class="bg-gray-300 rounded-sm"> <label>Tyre Patch</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.mushroom_patch" class="bg-gray-300 rounded-sm"> <label>Mushroom Patch</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.ac_service" class="bg-gray-300 rounded-sm"> <label>AC Service</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.battery" class="bg-gray-300 rounded-sm"> <label>Battery</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.wiper" class="bg-gray-300 rounded-sm"> <label>Wiper</label>
                                            </div>
                                            <div>
                                                <input type="checkbox" v-model="serviceDetails.car_wash" class="bg-gray-300 rounded-sm"> <label>Car Wash</label>
                                            </div>
                                        </div>
                                        <div>
                                            <button class="bg-green-500 w-[100%]  text-white font-bold 0 text-base p-4 rounded-lg m-3" @click="handleCustomer">Save</button>
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
                                        <input type="text" v-if="check" v-model="responseData.message[1].name"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter your Vehicle Number">
                                    </p>
                                    <p class="m-2">Owner Name <br>
                                        <input type="text" v-if="check" v-model="responseData.message[1].current_owner"
                                            class="w-[22rem] h-[3rem] bg-gray-300 mt-1 rounded-sm border-solid border border-black"
                                            placeholder="Enter your Owner Name">
                                    </p>
                                    <p class="m-2">Owner Mobile No <br>
                                        <input type="text" v-if="check"
                                            v-model="responseData.message[1].owner_mobile_no"
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
                                            <input type="text" v-model="employee.mobile_no"
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
                                            <input type="text" v-model="contact.contact_person_mobile"
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
                                            class="bg-blue-500 w-[100px] text-white font-bold 0 text-base p-5 rounded-lg ml-3"
                                            @click="modifiedMoreEmployee('current_driver')">Add Driver</button>

                                        <button
                                            class="bg-blue-500 w-[100px]  text-white font-bold 0 text-base p-4 rounded-lg ml-3"
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
                        <button class="text-[1.2rem]  text-white w-[12rem] h-[3rem] bg-blue-500 rounded-lg"
                            @click="addTyre">Add</button>
                    </div>
                    <hr class="mt-2 " :style="{ borderWidth: '2px', borderColor: 'gray' }">
                    <div class="grid grid-row space-y-5 mt-4  p-4 mr-[0.1rem] bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg"
                        v-for="(tyreData, index) in tyreDatas" :key="index">
                        <div class="flex">
                            <div class="grid grid-cols-4 w-[90%] gap-4">
                                <div class="flex flex-col space-y-1 ml-4">
                                    <label class="mt-2" :for="'tyre' + index">Tyre</label>
                                    <select class="w-[100%] h-[100%] rounded-sm" v-model="tyreData.tyre"
                                        :id="'type' + index" style="border: 1px solid black;"
                                        @change="updateTyreData(index)">
                                        <option value="" selected disabled hidden>Please select...</option>
                                        <option value="Front-Left">Front-Left</option>
                                        <option value="Front-Right">Front-Right</option>
                                        <option value="Back-Left">Back-Left</option>
                                        <option value="Back-Right">Back-Right</option>
                                        <option value="Stephanie">Spare-wheel</option>
                                    </select>
                                </div>
                                <div class="flex flex-col space-y-1">
                                    <label class="mt-2" :for="'RTD' + index">Remaining Tread Depth</label>
                                    <input v-model="tyreData.depth"
                                        class="w-[100%] h-[100%] rounded-sm border-solid border border-black"
                                        type="text" :id="'RTD' + index" @change="updateTyreData(index)">
                                </div>
                                <div class="flex flex-col space-y-1">
                                    <label class="mt-2" :for="'TP' + index">Tyre Pressure (psi)</label>
                                    <input v-model="tyreData.pressure"
                                        class="w-[100%] h-[100%] rounded-sm border-solid border border-black"
                                        type="text" :id="'TP' + index" @change="updateTyreData(index)">
                                </div>
                                <div class="flex flex-col space-y-1">
                                    <label class="mt-2" :for="'COM' + index">Comment</label>
                                    <input v-model="tyreData.comment"
                                        class="w-[100%] h-[100%] rounded-sm border-solid border border-black"
                                        type="text" :id="'COM' + index" @change="updateTyreData(index)">
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
                    <div class=" flex flex-row justify-between">
                        <h1 class="text-[20px] font-bold mb-1">Tyre Replacement Details</h1>
                        <button class="text-[1.2rem]  text-white w-[12rem] h-[3rem] bg-blue-500 rounded-lg"
                            @click="addTyreReplacement">Add</button>
                    </div>
                    <hr class="mt-2 " :style="{ borderWidth: '2px', borderColor: 'gray' }">
                    <div class="pb-5 ">
                        <div v-for="(tyre, index) in tyres" :key="index"
                            class="grid grid-cols-10 gap-[11rem] mt-7 pb-5 ml-2 border-b border-gray-900 p-2 bg-gray-200 rounded-lg shadow-md transition-shadow duration-300 hover:shadow-lg">
                            <div class="ml-5 w-[16rem]">
                                <label class="pt-2" :for="'type' + index">Tyer Position</label><br>
                                <select class="w-[15rem] h-[52px] rounded-sm border-solid border border-black"
                                    v-model="tyre.type" :id="'type' + index" @change="saveData(index)">
                                    <option value="" selected disabled hidden>Please select...</option>
                                    <option value="Front-Left">Front-Left</option>
                                    <option value="Front-Right">Front-Right</option>
                                    <option value="Back-Left">Back-Left</option>
                                    <option value="Back-Right">Back-Right</option>
                                    <option value="Stephanie">Spare-wheel</option>
                                </select>
                                <!-- <p class="text-[20px] font-bold mt-8">{{ position }} Tyre</p> -->
                                <div class="mt-[20px]">
                                    <label :for="'loadIndex' + index">Load Index</label><br>
                                    <input class="w-[15rem] h-[52px] rounded-sm border-solid border border-black"
                                        :id="'loadIndex' + index" type="text" v-model="tyre.loadIndex"
                                        @change="saveData(index)">
                                </div>
                            </div>
                            <div class="ml-[100px]">
                                <div>
                                    <label :for="'brand' + index">Brand</label>
                                    <input class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                        :id="'brand' + index" type="text" v-model="tyre.brand"
                                        @change="saveData(index)">
                                </div>
                                <div class="mt-[20px] w-[16rem]">
                                    <label :for="'speedRating' + index">Speed Rating</label>
                                    <input class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                        :id="'speedRating' + index" type="text" v-model="tyre.speedRating"
                                        @change="saveData(index)">
                                </div>
                            </div>
                            <div class="ml-[200px]">
                                <div>
                                    <label :for="'pattern' + index">Pattern</label>
                                    <input class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                        :id="'pattern' + index" type="text" v-model="tyre.pattern"
                                        @change="saveData(index)">
                                </div>
                                <div class="mt-[20px]">
                                    <label :for="'size' + index">Size</label>
                                    <input class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                        :id="'size' + index" type="text" v-model="tyre.size" @change="saveData(index)">
                                </div>
                            </div>
                            <div class="ml-[300px]">
                                <div>
                                    <label :for="'ttTl' + index">TT/TL</label>
                                    <input :id="'ttTl' + index"
                                        class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                        type="text" v-model="tyre.ttTl" @change="saveData(index)">
                                </div>
                                <div class="mt-[20px]">
                                    <label :for="'item' + index">Item</label>
                                    <input class="w-[16rem] h-[52px] rounded-sm border-solid border border-black"
                                        :id="'item' + index" type="text" v-model="tyre.item" @change="saveData(index)">
                                </div>
                            </div>
                            <div class="ml-[400px]">
                                <FeatherIcon name="x" class="mt-0 ml-2 w-6 h-6 cursor-pointer text-red-500"
                                    @click="deleteTyreReplacement" />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Billing Details -->
            <div v-if="currentstep == 4">
                <div class="pt-24 p-12">
                    <h1 class="text-[20px] font-bold mb-1">Raw Materials</h1>
                    <hr class="mt-2" :style="{ borderWidth: '2px', borderColor: 'gray' }">
                    <div class="pt-5">
                        <table
                            class="table-auto border border-collapse border-gray-800 w-auto shadow-md transition-shadow">
                            <thead>
                                <tr>
                                    <th class="border border-gray-800 px-4 py-4 w-[10rem]">SI.No</th>
                                    <th class="border border-gray-800 px-4 py-4 w-[10rem]">Item Code</th>
                                    <th class="border border-gray-800 px-4 py-4 w-[16rem]">Source Warehouse</th>
                                    <th class="border border-gray-800 px-4 py-4 w-[16rem]">Required Quantity</th>
                                    <th class="border border-gray-800 px-4 py-4 w-[10rem]">Rate</th>
                                    <th class="border border-gray-800 px-4 py-4 w-[10rem]">Cost</th>
                                </tr>
                            </thead>
                            <tbody class="border border-gray-800 text-center">
                                <tr v-for="(data, index) in tableData" :key="index">
                                    <td class="border border-gray-800 px-4 py-2 w-[10rem]">{{ index + 1 }}</td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <input type="text" v-model="data.itemCode"
                                            class="w-[10rem] rounded-sm border-solid border border-black">
                                    </td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <input type="text" v-model="data.sourceWarehouse"
                                            class="w-[10rem] rounded-sm border-solid border border-black">
                                    </td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <input type="text" v-model="data.requiredQuantity" @input="calculateTotals"
                                            class="w-[10rem] rounded-sm border-solid border border-black">
                                    </td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <input type="text" v-model="data.rate" @input="calculateTotals"
                                            class="w-[10rem] rounded-sm border-solid border border-black">
                                    </td>
                                    <td class="border border-gray-800 px-4 py-2">
                                        <input type="text" v-model="data.cost" readonly
                                            class=" w-[10rem] rounded-sm border-solid border border-black">
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
                                    <td class="border border-gray-800 px-4 py-2 text-center">
                                        {{ totalQuantity }}
                                    </td>
                                    <td colspan="" class="border border-gray-800 px-4 py-2 text-center">
                                        {{ totalRate.toFixed(2) }}
                                    </td>
                                    <td colspan="2" class="border border-gray-800 px-4 py-2 text-center">
                                        {{ totalCost.toFixed(2) }}
                                    </td>
                                </tr>
                            </tfoot>
                        </table>
                        <div class="mb-9">
                            <button class="bg-blue-500 text-white font-bold text-base p-3 rounded-lg mt-3"
                                @click="addNewRow">Add row</button>
                        </div>
                        <div class="flex">
                            <label>Discount Rate: <input type="text" v-model="discountRate"
                                    @input="calculateDiscountRate"
                                    class="w-[338px] h-[52px] rounded-sm border-solid border border-black"></label>
                            <label class="ml-auto pr-5">Final Amount: <input type="text" v-model="finalAmount" readonly
                                    class="w-[338px] h-[52px] rounded-sm border-solid border border-black"></label>
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
                    <button v-if="currentstep != 4"
                        class="bg-blue-500 w-[45%] text-white font-bold  text-base p-4 rounded-lg"
                        @click="nextPageAndHighlight">Next
                    </button>
                </div>
                <div class="bottom-div">
                    <div class="m-0 p-4">
                        <ul class="ml-[100px] flex space-x-[120px] text-center">
                            <li type="disc" :class="{ 'active': currentPage === 'details' }"
                                @click="setCurrentPage('details', 0)">Details</li>
                            <li type="disc" :class="{ 'active': currentPage === '5 Points Checkup' }"
                                @click="setCurrentPage('5 Points Checkup', 1)">5 Points Checkup</li>
                            <li type="disc" :class="{ 'active': currentPage === 'Required Services' }"
                                @click="setCurrentPage('Required Services', 2)">Required Services</li>
                            <li type="disc" :class="{ 'active': currentPage === 'Tyre Replacement Details' }"
                                @click="setCurrentPage('Tyre Replacement Details', 3)">Tyre Replacement Details</li>
                            <li type="disc" :class="{ 'active': currentPage === 'Billing Details' }"
                                @click="setCurrentPage('Billing Details', 4)">Billing Details</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive, watch,computed } from 'vue';
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

const pin1 = ref('');
const pin2 = ref('');
const pin3 = ref('');
const pin4 = ref('');

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

const jobCard =[]
//==========================================================>>> Main Page <<<================================================================================//

const isEditMode = ref(false)
const searchQuery = ref('');
const responseData = ref({});

const spacing = (plate) => {
    console.log('space checking', plate);
    const spaced_plate = plate.match(/[a-zA-Z]{1,2}|\d+/g).join(" ");
    console.log('after spacing :', spaced_plate);
    return spaced_plate;
};
const check = ref(false)
const search = async () => {
    const data = {
        "license_plate": searchQuery.value
    };
    console.log('checking data', data);
    try {
        if (data.license_plate.trim() !== "") {
            const response = await axios.post("http://192.168.1.39:8002/api/method/tyre.api.get_details", data);
            if (response.data.message === "") {
                alert("No data found");
                check.value = false;
                console.log(response.data);
            } else {
                check.value = true;
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
                        }, response.data.message[2]
                    ]
                };
                console.log("Response:", response.data);
            }
        } else {
            alert("Please enter search value");
            console.log("Please enter search value");
        }
    } catch (error) {
        console.error("Error:", error);
    }
};

const currentPage = ref('details');
// const currentstep = ref(0);
const maxStep = 4;

function previousPage() {
    if (currentstep.value > 0) {
        currentstep.value--;
        currentPage.value = getPageName(currentstep.value);
    }
}

function nextPageAndHighlight() {
    if (currentstep.value < maxStep) {
        currentstep.value++;
        currentPage.value = getPageName(currentstep.value);
        // if (currentstep.value == 3) {
        //     checkup(requireService)
        // }
        switch(currentstep.value){
            case 1:
            jobCard[0]=responseData.value;
                console.log(jobCard)
                break;
            case 2:
                jobCard[1]=tyreDatas.value;
                console.log(jobCard)
                break;
            case 3:
                jobCard[2]=requireService.value
                console.log(jobCard)
                break;
            case 4:
                checkup(jobCard)
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
    currentPage.value = page;
    currentstep.value = step;
}
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

const addVehicleData = async () => {
    const fieldNames = Object.keys(vehicleData.value);
    const data = {};

    fieldNames.forEach(fieldName => {
        const value = vehicleData.value[fieldName].trim();
        if (value == '') {
            return
        }
        data[fieldName] = value;
    });
    console.log(data);
    const json_data = { data: JSON.stringify(data) }
    console.log(json_data);
    console.log('vehicle number:', data.name);
    const isVehicleExist = await returnSearch(data.name)
    console.log('isvehicle exist :', isVehicleExist.message[0].name)
    if (isVehicleExist.message[0].name) {
        alert("Vehicle already Exist!")
        return
    }
    else {
        axios.post("http://192.168.1.39:8002/api/method/tyre.api.store_vehicle_details", json_data)
            .then(response => {
                console.log('vehicle add after response', response);
                if (responseData.value && responseData.value.message) {
                    check.value = true;
                    responseData.value = {
                        message: [
                            response.data.message[0],
                            response.data.message[1] === "" ? 'no data' : {
                                current_owner: '',
                                owner_mobile_no: '',
                                current_driver: [{
                                    current_driver: '',
                                    name: '',
                                    mobile_no: ''
                                }],
                                contact_person: [{
                                    contact_person_name: '',
                                    contact_person_mobile: ''
                                }]
                            }
                        ]
                    }
                    console.log("vehicle data in responseData.value:", responseData.value.message[0].alignment);
                    console.log("vehicle data in responseData.value:", responseData.value.message[0].name);
                    console.log("vehicle data in responseData.value:", responseData.value.message[0])
                    console.log("vehicle data in responseData.value:", responseData.value)
                    alert("Successfully added Vehicle!")

                } else {
                    check.value = false;
                    console.error("responseData.value or responseData.value.message is undefined");
                }
            })
            .catch(error => {
                console.error(error);
            });
    }
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
        const json_data = { data: JSON.stringify(modifiedData) }
        const response = await axios.post("http://192.168.1.39:8002/api/method/tyre.api.store_vehicle_details", json_data);
        console.log(response);
        returnSearch(name)
        alert("Successfully Modified Vehicle Data!")
    } catch (error) {
        console.error(error);
    }
};

const updateEmployeeType = (employee) => {
    console.log(employee);
    return employee.parentfield
}

const employees = ref([{
    driver_name: '',
    type: '',
    mobile_no: '',
    whatsappChecked1: 0,
    callChecked1: 0,
    smsChecked1: 0,
    primary: 0
}]);

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
            responseData.value.message[1].current_driver.push(newEmployee);
        } else if (type === 'contact_person') {
            const lastContactIndex = responseData.value.message[1].contact_person.length - 1;
            newEmployee.custom_whatsapp = responseData.value.message[1].contact_person[lastContactIndex]?.custom_whatsapp;
            newEmployee.custom_call = responseData.value.message[1].contact_person[lastContactIndex]?.custom_call;
            newEmployee.custom_sms = responseData.value.message[1].contact_person[lastContactIndex]?.custom_sms;
            responseData.value.message[1].contact_person.push(newEmployee);
        } else {
            console.error('Invalid employee type:', type);
            return;
        }
    } catch (error) {
        console.error('Error adding more employees:', error);
    }
};

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
    const name = customerData.value.name.trim();
    const existingData = await returnSearch(name);
    console.log('filtering process', existingData.message[1].current_owner);
    console.log('vehicle number during customer add:', existingData.message[0].name);
    if (!existingData.message[0].name) {
        console.log("Vehicle not exist!");
        alert("Vehicle not exist!")
        return
    }
    else if (existingData.message[0].name && !existingData.message[1].current_owner) {
        const ownerName = customerData.value.current_owner.trim();
        const ownerMobile = customerData.value.owner_mobile_no.trim();

        if (!ownerName && !ownerMobile && !name) {
            alert("Please fill in at least one of the fields: Owner Name or Owner Mobile");
            return;
        }
        if (employees.value.length === 0) {
            alert("Please add at least one employee");
            return;
        }
        const isAnyEmployeeDataMissing = employees.value.some(employee => {
            return !employee.driver_name.trim() || !employee.mobile_no.trim();
        });
        if (isAnyEmployeeDataMissing) {
            alert("Please fill in all fields for all employees");
            return;
        }
        // const primaryDriverCount = employees.value.filter(employee => employee.primary).length;
        // if (primaryDriverCount !== 1) {
        //     alert("Please select exactly one primary driver.");
        //     return;
        // }
        const data = {
            current_owner: customerData.value.current_owner,
            owner_mobile_no: customerData.value.owner_mobile_no,
            name: customerData.value.name,
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
        const json_data = { data: JSON.stringify(data) }
        console.log('before checking customer json_data', json_data);
        console.log(json_data);
        try {
            const response = await axios.post("http://192.168.1.39:8002/api/method/tyre.api.store_customer_details", json_data)
            check.value = true;
            console.log(response);
            if (responseData.value && responseData.value.message) {
                responseData.value = {
                    message: [
                        response.data.message[0] === "" ? 'no data' : {
                            name: 'No data',
                            vehicle_brand: 'No data',
                            vehicle_model: '',
                            chassis_no: '',
                            fuel_type: '',
                            last_odometer_reading: '',
                            tyre_change: '',
                            alignment: ''
                        },
                        response.data.message[1]
                    ]
                }
                alert("Successfully added customer data!")
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
            // Object.keys(customerData.value).forEach(key => {
            //     customerData.value[key] = '';
            // });
            // employees.value = [{ name: '', type: '', mobile_no: ''}];

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
        alert("Customer already added to this vehicle!")
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
            alert("Enter Driver name!")
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
            alert("Enter Contact Person name!")
            return
        }
        i += 1;
        console.log('index contact', i);
    });

    console.log('modify checking', modifiedData);
    const json_data = { data: JSON.stringify(modifiedData) };
    console.log("Modified data", json_data)
    try {
        const response = await axios.post("http://192.168.1.39:8002/api/method/tyre.api.store_customer_details", json_data);
        check.value = true;
        console.log(response);
        returnSearch(name)
        alert("Successfully Modified customer data!")

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

const handle = ref(false);
const size = ref('');
const selectedBrand = ref('');
const quantity = ref('');
const serviceDetails = ref({
    alignment:0,
    oil_change:0,
    inflation:0,
    tyre_edge:0,
    mushroom_patch:0,
    battery:0,
    car_wash:0,
    rotation:0,
    balancing:0,
    puncture:0,
    tyre_patch:0,
    ac_service:0,
    wiper:0
})

const handleCustomer =async ()=>{
    const customerDetails = {
        current_owner:customerData.value.current_owner,
        owner_mobile_no:customerData.value.owner_mobile_no,
        size:size.value,
        selectedBrand:selectedBrand.value,
        whatsapp:customerData.value.whatsappChecked,
        call:customerData.value.callChecked,
        sms:customerData.value.smsChecked,
    }
    console.log("checking Customer Details",customerDetails)
    try {
        const json_data = { data: JSON.stringify(customerDetails) };
        // console.log('checking customer details',json_data);
        // const response = await axios.post("http://192.168.1.39:8002/api/method/tyre.api.store_customer_details", json_data)
        // console.log('response from customer details',response.data);

    } catch (error) {
        
    }
}

const handleEnquiry = async () => {
    try {
        const response = await axios.get("http://192.168.1.39:8002/api/method/tyre.api.stock_details");
        console.log('response data for customer details', response.data);
        responseData.value = response.data;
        console.log(responseData.value);
        
        // Assuming responseTyreData.value.message is an array of objects
        for (let tyre of responseData.value.message) {
            console.log(tyre.name);
        }
    } catch (error) {
        console.error('Error fetching tyre data:', error);
    }
};

const clearVehicleData = () => {
    Object.keys(vehicleData.value).forEach(key => {
        vehicleData.value[key] = '';
    });
};

const returnSearch = async (search) => {
    const data = {
        "license_plate": search
    };
    console.log('checking data', data);
    try {
        if (data.license_plate.trim() !== "") {
            const response = await axios.post("http://192.168.1.39:8002/api/method/tyre.api.get_details", data);
            check.value = true;
            console.log('returnSearch data', response);
            if (response.data.message === "") {
                responseData.value = {
                    message: [{
                        name: '',
                        vehicle_brand: '',
                        vehicle_model: '',
                        chassis_no: '',
                        fuel_type: '',
                        last_odometer_reading: '',
                        tyre_change: '',
                        alignment: ''
                    },
                    {
                        current_owner: '',
                        owner_mobile_no: '',
                        current_driver: [{
                            current_driver: '',
                            name: '',
                            mobile_no: ''
                        }],
                        contact_person: [{
                            contact_person_name: '',
                            contact_person_mobile: ''
                        }]
                    }]
                };
                console.log(response.data);
                return responseData.value;
            } else {
                responseData.value = response.data;
                console.log('cutomer details checking now', responseData.value);
                return responseData.value;
            }
        } else {
            alert("Please enter search value");
            console.log("Please enter search value");
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
    responseData.value.message[1].current_driver.splice(index, 1);
};
const removeEmployee3 = (index) => {
    responseData.value.message[1].contact_person.splice(index, 1);
};
const removeEmployee1 = (index) => {
    employees.value.splice(index, 1);
};


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
    console.log('Updated tyre data:', tyre);
    console.log(tyreDatas.value);
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
    console.log(data.value)
    const json_data = { data: JSON.stringify(data.value) }
    console.log(json_data);
    // try {
    //     const response = axios.post("http://192.168.1.39:8002/api/method/tyre.api.job_card", json_data);
    //     console.log(response);
    // } catch (error) {
    //     console.error("error");
    // }
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

// const tyres = ref(Array.from({ length: tyrePositions.length }, () => ({
//   loadIndex: '',
//   brand: '',
//   speedRating: '',
//   pattern: '',
//   size: '',
//   ttTl: '',
//   item: ''
// })));

const tyres = ref([{
    type: '',
    loadIndex: '',
    brand: '',
    speedRating: '',
    pattern: '',
    size: '',
    ttTl: '',
    item: ''
}]);

const saveData = (index) => {
    const tyreValues = tyres.value[index];
    console.log('Updated tyre data:', tyreValues);
    console.log(tyres.value);
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
            item: ''
        })
        setValue.index++;
    }
}
const deleteTyreReplacement = (index) => {
    if (setValue.index > 1) {
        tyres.value.splice(index, 1)
        setValue.index--;
    }
    //   tyres.value.splice(index, 1)
}

//===================================================>>> Billing Details <<<=========================================================================================//

const tableData = ref([{ itemCode: '', sourceWarehouse: '', rate: '', requiredQuantity: '', cost: '' }]);
const totalRate = ref(0);
const totalQuantity = ref(0);
const totalCost = ref(0);
const discountRate = ref();
const finalAmount = ref(0);

const calculateTotals = () => {
    let sumRate = 0;
    let sumQuantity = 0;
    let sumCost = 0;

    tableData.value.forEach(row => {
        const rate = parseFloat(row.rate) || 0;
        const quantity = parseFloat(row.requiredQuantity) || 0;
        row.cost = (rate * quantity).toFixed(2);
        sumRate += rate;
        sumQuantity += quantity;
        sumCost += rate * quantity;
    });

    totalRate.value = sumRate;
    totalQuantity.value = sumQuantity;
    totalCost.value = sumCost;

    calculateDiscountRate();
};

const calculateDiscountRate = () => {
    if (discountRate.value == 0) {
        finalAmount.value = totalCost.value;
        return
    }
    finalAmount.value = totalCost.value - discountRate.value;
};

const addNewRow = () => {
    tableData.value.push({
        sno: '',
        itemCode: '',
        sourceWarehouse: '',
        rate: '',
        requiredQuantity: '',
        cost: '',
    });
    calculateTotals();
};


const submitData = () => {
    console.log("hi", tableData.itemCode, totalRate, totalQuantity, totalCost, discountRate, finalAmount);
}
const removeRow = (index) => {
    tableData.value.splice(index, 1);
    calculateTotals();
};

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